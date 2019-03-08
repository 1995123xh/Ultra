# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 17:24:59 2018

@author: Hao
"""

# To parse water scan data
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

d_data_file = input('drag scan csv export file... ').replace('\\ ', ' ').strip("'").strip('"').strip()
d_data= pd.read_csv(d_data_file, sep = None, engine = 'python')
d_data_diff=d_data              #This is used to find where the significant height is passed. Initializing it here
peaktopidx=d_data['H4 CDD'].idxmax()
peaktop=d_data.loc[peaktopidx]
sigheight=0.7*peaktop['H4 CDD']
# =============================================================================
# d_data_diff.loc[:,'H4 CDD']=np.abs(d_data.loc[:,'H4 CDD']-sigheight)
# =============================================================================
sigpass1=d_data.loc[np.abs(d_data.loc[:,'H4 CDD']-sigheight)[:peaktopidx].idxmin()]
sigpass2=d_data.loc[np.abs(d_data.loc[:,'H4 CDD']-sigheight)[peaktopidx:].idxmin()]
peakcenter=np.average([sigpass1['Mass H4 CDD'], sigpass2['Mass H4 CDD']])

if peakcenter<17.5:
    stretchfactor=0.932644
else:
        stretchfactor=1
        
adduct=peakcenter+0.001374*stretchfactor
C13H3D=peakcenter+0.00292*stretchfactor

adductidx=np.abs(d_data.iloc[:,1]-adduct).idxmin()
C13H3Didx=np.abs(d_data.iloc[:,1]-C13H3D).idxmin()

adductfactor=d_data.loc[adductidx, 'H4 CDD']/peaktop['H4 CDD']
C13H3Dfactor=d_data.loc[C13H3Didx, 'H4 CDD']/peaktop['H4 CDD']

print('adduct factor=', adductfactor)
print('C13H3D factor=', C13H3Dfactor)
input('Press ENTER to exit ')
# =============================================================================
# Intensity=d_data['H4 CDD'].values
# diff=np.abs(Intensity-sigheight)
# =============================================================================


# =============================================================================
# d=d_data.values
# maxI=max(d[:,2])
# indexmax=a.index(maxI)
# =============================================================================
