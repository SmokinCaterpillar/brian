'''
Model fitting example using a cluster.

Fits an integrate-and-fire model to an in-vitro electrophysiological 
recording over one second.

This script is the 'manager' script and should be run after all the workers
have started.
'''
if __name__ == '__main__':
    from brian import *
    from brian.library.modelfitting import *
    
    equations = Equations('''
        dV/dt=(R*I-V)/tau : 1
        I : 1
        R : 1
        tau : second
    ''')
    
    input = loadtxt('current.txt')
    spikes = loadtxt('spikes.txt')
    
    # Change this line to the hostnames or IP addresses of the workers
    machines = ['localhost']
    
    params, gamma = modelfitting(model = equations, reset = 0, threshold = 1, 
                                 data = spikes, 
                                 input = input, dt = .1*ms,
                                 particles = 1000, iterations = 3, delta = 2*ms,
                                 R = [1.0e9, 1.0e10], tau = [1*ms, 50*ms],
                                 machines=machines, use_gpu=False, max_cpu=2)
    
    print params