# -*- coding: iso-8859-1 -*-
import math
import sys
import os

in_file=file('A-large.in')
out_file=file('A-large.out','w')

skim=sys.stdout
sys.stdout=out_file

def get_sw(se,qu):
	
	se_st={}
	for i in se:
		se_st[i]=0
	
	min_ch=0
	prev=-1
	for i_qu in qu:
		se_st[i_qu]=min_ch+1
		min_ch=1e10
		for i_se in se:
			if i_se!=prev and se_st[i_se]<min_ch: min_ch=se_st[i_se]
		prev=i_qu
		#print se_st
	
	return min_ch	

def get_sw_h(se,qu):
	
	se_st=[]
	len_se=len(se)
	#print len(se)
	min_ch=0
	for i_qu in qu:
		if i_qu not in se_st:
			se_st.append(i_qu)
		if len(se_st)>=len_se:
			min_ch+=1
			se_st=[i_qu]
		#print se_st
	
	return min_ch	
	
			
#se=['Y','N','D','B','G']
#qu=['Y','Y','G','B','G','N','B','N','D','G']
#print get_sw(se,qu)


i_line=0
state=0
i_case=0
for line in in_file:
	#print line.strip()
	kov=1==1
	if kov and state==0:
		kov=1==0
		state=1
		n_cases=int(line.strip())
		#print 'cases',n_cases
	if kov and state==1:
		kov=1==0
		state=2
		n_eng=int(line.strip())
		n_cases-=1
		se=[]
		qu=[]
		#print 'engines',n_eng
	if kov and state==2:
		kov=1==0
		n_eng-=1
		si_eng=line.strip()
		#print 'eng',si_eng
		se.append(si_eng)
		if n_eng<1: state=3
	if kov and state==3:
		kov=1==0
		state=4
		n_qu=int(line.strip())
		if n_qu==0: state=5
		#print 'n_qu',n_qu
	if kov and state==4:
		kov=1==0
		n_qu-=1
		si_qu=line.strip()
		#print 'qu',si_qu
		qu.append(si_qu)
		if n_qu<1: state=5
	if state==5:
		#print 'se',se
		#print 'qu',qu
		i_case+=1
		print 'Case #'+str(i_case)+': '+str(get_sw_h(se,qu))
		state=1
		
	i_line+=1

