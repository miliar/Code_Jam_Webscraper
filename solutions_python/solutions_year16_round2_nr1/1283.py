import random
import itertools

t = int(input())

m =  ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]


def fufu(n):
	c =  [0,0,0,0,0,0,0,0,0,0]
	di= {}
	n = list(n)
	n.sort()
	for i in n:
		if i in di.keys():
			di[i]= di[i]+1
		else:
			di[i]= 1
	if 'Z' in di.keys():
		if (di['Z']!=0):
			t = di['Z']
			di['Z']= di['Z']-t
			di['E']= di['E']-t
			di['R']= di['R']-t
			di['O']= di['O']-t
			c[0]=t
	if 'X' in di.keys():
		if (di['X']!=0):
			t = di['X']
			di['S']= di['S']-t
			di['I']= di['I']-t
			di['X']= di['X']-t
			c[6]=t
	if 'G'in di.keys():
		if (di['G']!=0):
			t = di['G']
			di['E']= di['E']-t
			di['I']= di['I']-t
			di['G']= di['G']-t
			di['H']= di['H']-t
			di['T']= di['T']-t
			c[8]=t
	if 'H' in di.keys():
		if (di['H']!=0):
			t = di['H']
			di['T']= di['T']-t
			di['H']= di['H']-t
			di['R']= di['R']-t
			di['E']= di['E']-(2*t)
			c[3]=t
	if 'W' in di.keys():
		if (di['W']!=0):
			t = di['W']
			di['T']= di['T']-t
			di['W']= di['W']-t
			di['O']= di['O']-t
			c[2]=t
	if 'S' in di.keys():
		if (di['S']!=0):
			t = di['S']
			di['S']= di['S']-t
			di['E']= di['E']-(2*t)
			di['V']= di['V']-t
			di['N']= di['N']-t
			c[7]=t
	if 'V' in di.keys():
		if (di['V']!=0):
			t = di['V']
			di['F']= di['F']-t
			di['I']= di['I']-t
			di['V']= di['V']-t
			di['E']= di['E']-t
			c[5]=t
	if 'F' in di.keys():
		if (di['F']!=0):
			t = di['F']
			di['F']= di['F']-t
			di['O']= di['O']-t
			di['U']= di['U']-t
			di['R']= di['R']-t
			c[4]=t
	if 'O' in di.keys():
		if (di['O']!=0):
			t = di['O']
			di['O']= di['O']-t
			di['N']= di['N']-t
			di['E']= di['E']-t
			c[1]=t
	if 'E' in di.keys():
		if (di['E']!=0):
			t = di['E']
			di['N']= di['N']-2*t
			di['I']= di['I']-t
			di['E']= di['E']-t
			c[9]=t
		
	s=''
	#print (c)
	for i in range(0,10):
		for j in range(0,c[i]):
			s=s+str(i)
	return s


for i in range(1,t+1):
	s = input()
	#print (s)
	print ("Case #{}: {}".format(i,fufu(s)))
