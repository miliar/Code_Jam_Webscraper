case=int(input())
a=1
while case>=a:
	y=0
	z=0
	dir_namoi={}
	dir_ken={}
	dk=[]
	dn=[]
	number=int(input())
	mass_namoi=input().split(' ')
	mass_ken=input().split(' ')
	for i in range(0,number):
		mass_namoi[i]=float(mass_namoi[i])
		mass_ken[i]=float(mass_ken[i])
	mass_namoi.sort()
	mass_ken.sort()
	for i in range(0,number):
		dn=[]
		for j in range(0,number):
			if mass_namoi[i]>mass_ken[j]:
				dn.append(mass_ken[j])
		dir_namoi[mass_namoi[i]]=dn
	for i in range(0,number):
		if len(dir_namoi[mass_namoi[i]])>0:
			y+=1
			for j in range(i+1,number):
				dir_namoi[mass_namoi[j]]=list(set(dir_namoi[mass_namoi[j]])-{dir_namoi[mass_namoi[i]][0]})
	for i in range(0,number):
		dk=[]
		for j in range(0,number):
			if mass_ken[i]>mass_namoi[j]:
				dk.append(mass_namoi[j])
		dir_ken[mass_ken[i]]=dk
	for i in range(0,number):
		if len(dir_ken[mass_ken[i]])>0:
			z+=1
			for j in range(i+1,number):
				dir_ken[mass_ken[j]]=list(set(dir_ken[mass_ken[j]])-{dir_ken[mass_ken[i]][0]})
	print("Case #"+str(a)+":",y,(number-z))		
	a+=1
				
	
	
