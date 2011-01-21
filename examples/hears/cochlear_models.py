'''
Example of the use of the cochlear models available in the library
'''
from brian import *
set_global_preferences(useweave=True)
from brian.hears import *

simulation_duration=50*ms
samplerate=50*kHz
sound = whitenoise(simulation_duration,samplerate)
sound=sound.atlevel(50*dB) # dB level in rms dB SPL
cf=erbspace(100*Hz, 1000*Hz, 50)

## DNRL
param_drnl={}
param_drnl['lp_nl_cutoff_m']=1.1

drnl_filter=DRNL(sound,cf,type='human',param=param_drnl)
drnl=drnl_filter.process()

## CDGC
param_cdgc={}
param_cdgc['c1']=-2.96
interval=1
cdgc_filter=DCGC(sound,cf,interval,param=param_cdgc)
cdgc=cdgc_filter.process()


figure()
subplot(211)
imshow(flipud(drnl.T),aspect='auto')
subplot(212)
imshow(flipud(cdgc.T),aspect='auto')


show()