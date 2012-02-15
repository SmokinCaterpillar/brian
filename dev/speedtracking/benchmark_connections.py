from vbench.benchmark import Benchmark
from datetime import datetime

common_setup = """
from brian import *
"""

setup_template = """
s = arange(%(neurons)d)
class thr(Threshold):
    def __call__(self, P):
        return s
G = NeuronGroup(%(neurons)d, 'V:1', threshold=thr())
H = NeuronGroup(%(neurons)d, 'V:1')
C = Connection(G, H, structure='%(structure)s' )
C.connect_full(G, H, weight=1)
net = Network(G, H, C)
net.prepare()
net.run(defaultclock.dt)
"""

statement = "net.run(1 * second)"

bench_sparse = Benchmark(statement,
                         common_setup + (setup_template % {'neurons' : 10,
                                                           'structure' : 'sparse'}),
                         name='sparse connection matrix (10x10)')

# Set a start date here because the benchmark fails for earlier revisions
bench_dynamic = Benchmark(statement,
                          common_setup + (setup_template % {'neurons' : 5,
                                                            'structure' : 'dynamic'}),
                          name='dynamic connection matrix (5x5)',
                          start_date = datetime(2010, 2, 4))

bench_dense = Benchmark(statement,
                        common_setup + (setup_template % {'neurons' : 10,
                                                          'structure' : 'dense'}),
                        name='dense connection matrix (10x10)')

