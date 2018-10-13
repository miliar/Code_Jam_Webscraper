# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 16:35:32 2015

@author: colorbox
"""
from __future__ import print_function
flip=open('C:\Users\colorbox\Desktop\cod_jam_qual\output.txt', 'w')
file_in=r'C:\Users\colorbox\Desktop\cod_jam_qual\A-small-attempt0.in'
with open(file_in) as f:
    rows=f.readlines()
output=[]   
for i in range(1,int(rows[0])+1):
    workspace=rows[i].split(' ')
    value=workspace[1]
    n_friends=0
    thresh=0
    human_tot=0
    value=value.replace('\n','')
    for j in range(len(value)):
        current_val=int(value[j])
        if current_val>0:
            if human_tot<thresh:
                n_friends+=thresh-human_tot
                human_tot+=n_friends
            human_tot+=current_val
        thresh+=1
    print( 'Case #'+str(i)+': '+str(n_friends),file=flip)
flip.close()
            