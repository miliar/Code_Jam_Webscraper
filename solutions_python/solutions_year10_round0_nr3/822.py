

import pdb

archivo=open('input.in','r')


T=int(archivo.readline())

for i in range(0,T):
	lista=archivo.readline().split(' ')
	R=int(lista[0])
	k=int(lista[1])
	N=int(lista[2])
	groups=archivo.readline().split(' ')
	rollercoaster=[]
	index=0
	costo=0
	for u in range(0,R):
		people=0
		Flag_terminado=False
		for x in range(index,N):
			people+=int(groups[x])
			if people<=k:
				rollercoaster.append(int(groups[x]))
			else:
				people-=int(groups[x])
				Flag_terminado=True
				break
		if Flag_terminado==False:
			for x in range(0,index):
				people+=int(groups[x])
				if people<=k:
					rollercoaster.append(int(groups[x]))
				else:
					people-=int(groups[x])
					Flag_terminado=True
					break
			
		index=x
		costo+=people
	print 'Case #'+str(i+1)+':',costo


