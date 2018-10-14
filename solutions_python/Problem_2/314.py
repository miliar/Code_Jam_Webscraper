# -*- coding: iso-8859-1 -*-
import math
import sys
import os
import pickle

in_file=file('B-large.in')
out_file=file('B-large.out','w')

skim=sys.stdout
sys.stdout=out_file

def obj_copy(obj):
	s=pickle.dumps(obj)
	return pickle.loads(s)

def h_m(t1):
	m_hour=int(t1)/100
	m_min=t1-(m_hour)*100
	return m_hour*60+m_min

class train:
	def __init__(self,ut,dep,arr):
		self.ut=ut
		self.dep=dep
		self.arr=arr
		
	def kapcsol(self,train2,TA):
		train3=train('',3000,0)
		if self.ut[-1]==train2.ut[0]:
			if self.arr+TA<=train2.dep:
				train3=train(self.ut+train2.ut,self.dep,train2.arr)
		return train3
		
	def __cmp__(self,train2):
		return self.dep-train2.dep
			
	def kiir(self):
		print self.ut,self.dep,self.arr

class tr2(train):
	def __init__(self,ut,dep,arr):
		self.ut=ut
		self.dep=h_m(dep)
		self.arr=h_m(arr)

def indulas(TA,time_table):
	
	time_table.sort()
	vonatok={}
	for i_tt in time_table: 
		#print 'i_tt',
		#i_tt.kiir()
		if len(vonatok)<1:
			#print 'Elso vonat'
			vonatok[len(vonatok)]=i_tt
		else:
			uj_vonatok=obj_copy(vonatok)
			kapcsolat=1!=1
			vonatkeys=vonatok.keys()
			vonatkeys.sort()
			for i_vonat in vonatkeys:
				#print 'i_vonat', 
				#vonatok[i_vonat].kiir()
				v3=vonatok[i_vonat].kapcsol(i_tt,TA)
				if v3.dep<1800:
					#print 'Van kapcsolat'
					uj_vonatok[i_vonat]=v3
					kapcsolat=1==1
					break
				else:
					pass
					#print 'nincs kapcsolat'
			if not kapcsolat: uj_vonatok[len(vonatok)]=i_tt
			vonatok=obj_copy(uj_vonatok)
		#print 'vonatok'
		#for i in vonatok:
			#vonatok[i].kiir()
	#print 'vonatok'
	indul={'A':0,'B':0}
	for i in vonatok:
		indul[vonatok[i].ut[0]]+=1
	#print indul
	return str(indul['A'])+' '+str(indul['B'])
		
#TA=5
#time_table=[tr2('AB',900,1200),tr2('AB',1000,1300),tr2('AB',1100,1230),tr2('BA',1202,1500),tr2('BA',900, 1030)]
#print indulas(TA,time_table)


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
		TA=int(line.strip())
		n_cases-=1
	if kov and state==2:
		kov=1==0
		n_A=int(line.strip().split(' ')[0].strip())
		n_B=int(line.strip().split(' ')[1].strip())
		#print 'TT',TA,n_A,n_B
		time_table=[]
		state=3
	if kov and state==3:
		#print 's3'
		kov=1==0
		if n_A>0:
			n_A-=1
			ind=int(line.strip().split(' ')[0].strip().replace(':',''))
			erk=int(line.strip().split(' ')[1].strip().replace(':',''))
			time_table.append(tr2('AB',ind,erk))
			if n_A<1 and n_B<1: state=4
		else:
			if n_B>0:
				n_B-=1
				ind=int(line.strip().split(' ')[0].strip().replace(':',''))
				erk=int(line.strip().split(' ')[1].strip().replace(':',''))
				time_table.append(tr2('BA',ind,erk))
				if n_B<1: state=4
			else:
				state=4
				
	
	
	if state==4:
		#for i in time_table:
		#	i.kiir()
			
		i_case+=1
		print 'Case #'+str(i_case)+': '+indulas(TA,time_table)
		state=1
		
	i_line+=1




