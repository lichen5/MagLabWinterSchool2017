
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
sns.set_style('whitegrid')
import glob,pickle
from runqmc import H2Runner,generate_dataframe

#--- Collect data
runners=[]
for filename in glob.glob("*.pickle"):
  with open(filename,'rb') as f:
    runner=pickle.load(f)
    runners.append(runner)
df=pd.DataFrame(generate_dataframe(runners))
df.sort_values('r',inplace=True)


#--- Plot energy
groups=df.groupby('wavefunction')
args={'marker':'o','mew':1,'linestyle':'-'}
for a,b in groups:
  plt.errorbar(b['r'],b['slat_en'],b['slat_en_err'],label='Slater'+a,**args)
  plt.errorbar(b['r'],b['sj_en'],b['sj_en_err'],label='SJ' + a,**args)
  plt.errorbar(b['r'],b['dmc_en'],b['dmc_en_err'],label='DMC' + a,**args)
  
plt.xlabel("r (Bohr)")
plt.ylabel("Energy (Hartree)")
plt.legend(loc=(1.0,0.5))

sns.despine()
plt.savefig("energy.pdf",bbox_inches='tight')
