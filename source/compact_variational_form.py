import numpy as np
import scipy as sp

from qiskit import QuantumCircuit, QuantumRegister
from qiskit.aqua.components.variational_forms import VariationalForm

class CTHVarForm(VariationalForm):

    # Hardcoding this for H2
    def __init__(self, num_qubits=0, init_state=None):
        self._num_qubits = num_qubits
        self._init_state = init_state
        self._num_parameters = 1 


    def construct_circuit(self, parameters, q=None):

        if q is None:
            q = QuantumRegister(self._num_qubits, name='q')

        circuit = self._init_state.construct_circuit('circuit', q)
        
        circuit.u3(np.pi/2,-np.pi/2,np.pi/2, 0)
        circuit.u2(0,np.pi, 1)

        for i in range(self._num_qubits-1):
            circuit.cx(i,i+1)

        circuit.u1(parameters[0], -1)

        for i in range(self._num_qubits-2, -1, -1):
            circuit.cx(i,i+1)

        circuit.u3(-np.pi/2,-np.pi/2,np.pi/2, 0)
        circuit.u2(0,np.pi, 1)
        return circuit
