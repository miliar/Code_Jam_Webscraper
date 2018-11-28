#!/usr/bin/python
# Google code 2013
max=2**15
inf = open('input.txt')
outf = open('output.txt','w')
t = inf.readlines()
n = int(t[0].rstrip())
global str

chisl = 1



def str_invers(str):
	return str[::-1]
	

def in_range(ch):
	f=0
	global g
	while (f<n):
		if((ch>=g[3*f])&(ch<=g[3*f+1])):
			g[f*3+2]=g[f*3+2]+1
		f=f+1
	return 1


i=0
g =[]
while i<n:
	e=t[i+1].rstrip().split(' ')
	e[0]=int(e[0])**0.5
	e[1]=int(e[1])**0.5
	e[len(e):]=[0]
	g[len(g):]=e
	i=i+1
i=0
while i<n:
	if ((g[i*3]<=1)&(g[i*3+1]>=1)):
		g[i*3+2]=g[i*3+2]+1
	if ((g[i*3]<=2)&(g[i*3+1]>=2)):
		g[i*3+2]=g[i*3+2]+1
	if ((g[i*3]<=3)&(g[i*3+1]>=3)):
		g[i*3+2]=g[i*3+2]+1
	if ((g[i*3]<=22)&(g[i*3+1]>=22)):
		g[i*3+2]=g[i*3+2]+1
	i=i+1

i=1
while i<max:
	if ((bin(i)[-2]==0)|(i<3)):
		ch=int(bin(i)[2:]+"2"+str_invers(bin(i)[2:]))
		f=0
		while (f<n):
			if((ch>=g[3*f])&(ch<=g[3*f+1])):
				g[f*3+2]=g[f*3+2]+1
			f=f+1
	ch=int(bin(i)[2:]+"0"+str_invers(bin(i)[2:]))
	f=0
	while (f<n):
		if((ch>=g[3*f])&(ch<=g[3*f+1])):
			g[f*3+2]=g[f*3+2]+1
		f=f+1
	ch=int(bin(i)[2:]+"1"+str_invers(bin(i)[2:]))
	f=0
	while (f<n):
		if((ch>=g[3*f])&(ch<=g[3*f+1])):
			g[f*3+2]=g[f*3+2]+1
		f=f+1
	ch=int(bin(i)[2:]+str_invers(bin(i)[2:]))
	f=0
	while (f<n):
		if((ch>=g[3*f])&(ch<=g[3*f+1])):
			g[f*3+2]=g[f*3+2]+1
		f=f+1
	i=i+1

i=0
while i<n:
	outf.write("Case #"+str(i+1)+": "+str(g[i*3+2])+'\n')
	i=i+1