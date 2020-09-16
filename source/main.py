import sys

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt


from qiskit.circuit import Parameter
from qiskit.chemistry.core import Hamiltonian, TransformationType, QubitMappingType
from qiskit.compiler import transpile

from QiskitVQEWrapper.vqe_wrapper.VQE_wrapper import VQEWrapper
from compact_variational_form import CTHVarForm

wrapper = VQEWrapper()

wrapper.molecule_string = "H 0.0 0.0 0.0; H 0.735 0.0 0.0"
wrapper.spin = 0
wrapper.charge = 0
wrapper.qubit_mapping = QubitMappingType.PARITY
wrapper.two_qubit_reduction = True

#print('\n\nOnly single excitations:')
#wrapper.excitation_type = 's'
#wrapper.initiate()
#results = wrapper.run_vqe()
#params = [Parameter(f'a_{i}') for i in range(wrapper.vqe_algo.var_form.num_parameters)]
#qc = wrapper.vqe_algo.construct_circuit(params)[0]
#print(qc.decompose())
#qc.draw()
#print(results)
#
#print('\n\nOnly double excitations:')
#wrapper.excitation_type = 'd'
#wrapper.initiate()
#results = wrapper.run_vqe()
#params = [Parameter(f'a_{i}') for i in range(wrapper.vqe_algo.var_form.num_parameters)]
#qc = wrapper.vqe_algo.construct_circuit(params)[0]
#print(qc.decompose())
#qc.draw()
#print(results)
#
#print('\n\nSingle and double excitations:')
#wrapper.excitation_type = 'sd'
#wrapper.initiate()
#results = wrapper.run_vqe()
#params = [Parameter(f'a_{i}') for i in range(wrapper.vqe_algo.var_form.num_parameters)]
#qc = wrapper.vqe_algo.construct_circuit(params)[0]
#print(qc.decompose())
#qc.draw()
#print(results)


print('\n\nMy own variational ansatz:')
wrapper.ansatz = 'custom'
wrapper.initiate()
wrapper.var_form = CTHVarForm(2, wrapper.init_state)
wrapper.initiate()
results = wrapper.run_vqe()
params = [Parameter(f'$\\theta_{i}$') for i in range(wrapper.vqe_algo.var_form.num_parameters)]
qc = wrapper.vqe_algo.construct_circuit(params)[0]
print(qc.decompose())
transpiled_qc = transpile(qc.decompose(), basis_gates=['cz','rx','ry','rz'], optimization_level=3)
print(transpiled_qc)
qc.draw(output='latex', filename='results/CCD.png')
print(results)

plt.show()
