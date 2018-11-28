

import pdb

archivo=open('input.in','r')

T=int(archivo.readline())


for i in range(0,T):
	lista=archivo.readline().split(' ')
	N=int(lista[0])
	K=int(lista[1])
	snappers=[]
	for n in range(0,N):
		snappers.append(0)
	for k in range(0,K):
		w=0
		while snappers[w]:
			snappers[w]=not(snappers[w])
			if w==(len(snappers)-1):
				w+=1
				break
			w+=1
		if w<len(snappers):
			snappers[w]=not(snappers[w])
			
	result=True
	for a in snappers:
		if a==1:
			result = result and 1
		else:
			result=False
			break
	if result:
		print 'Case #'+str(i+1)+':', 'ON'
	else:
		print 'Case #'+str(i+1)+':', 'OFF'	
