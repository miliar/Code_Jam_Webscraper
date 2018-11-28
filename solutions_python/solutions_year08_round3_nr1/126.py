# -*- coding: iso-8859-1 -*-
import math
import sys
import os
import pickle

in_file=file('A-large.in')
out_file=file('A-large.out','w')

skim=sys.stdout
sys.stdout=out_file

def obj_copy(obj):
	s=pickle.dumps(obj)
	return pickle.loads(s)

def leutesek(n_P,n_K,n_L,lst):
	ism=[]
	for i_lst in lst: ism.append(int(i_lst))
	ism.sort()
	ism.reverse()
	i_K=n_K
	#print 'Q'
	szorzo=1
	szum=0
	for i_ism in ism:
		i_K-=1
		if i_K<0:
			i_K=n_K-1
			szorzo+=1
		#print i_ism,szorzo
		szum+=i_ism*szorzo
	return szum

	
i_line=0
state=0
i_case=0
for line in in_file:
	#print 'line:',line.strip()
	kov=1==1
	if kov and state==0:
		kov=1==0
		state=1
		n_cases=int(line.strip())
		#print 'cases',n_cases
	if kov and state==1:
		kov=1==0
		state=2
		lst=line.strip().split(' ')
		n_P=int(lst[0].strip())
		n_K=int(lst[1].strip())
		n_L=int(lst[2].strip())
		n_cases-=1
		#print n_P, n_K, n_L
	if kov and state==2:
		kov=1==0
		state=1
		i_case+=1
		lst=line.strip().split(' ')
		#print lst
		leut=leutesek(n_P,n_K,n_L,lst)
		print 'Case #'+str(i_case)+': '+str(leut)
		state=1
		
	i_line+=1




