def insert(root,temp):
	l=temp.split('/')
	i=1
	l1=len(l)
	tt=""
	while i<l1:
		tt+="/"+l[i]
		if root.has_key(tt):
			root=root
		else:
		 	root[tt]=1
		i+=1
	return root

def crate(temp,root):
	count=0
	l=temp.split('/')
	i=1
	l1=len(l)
	tt=""
	while i<l1:
		tt+="/"+l[i]
		if root.has_key(tt):
			root=root
		else:
		 	root[tt]=1
		 	count+=1
		i+=1
	return (root,count)
	
sun=input()
pra=0
while pra<sun:
	inp=raw_input()
	ll=inp.split(' ')
	N=int(ll[0])
	M=int(ll[1])
	create=[]
	i=0
	root={}
	while i<N:
		temp=raw_input()
		root=insert(root,temp)
		i+=1

	i=0
	while i<M:
		temp=raw_input()
		create.append(temp)
		i+=1


	count=0
	i=0
	while i<M:
		kk=crate(create[i],root)
		count+=kk[1]
		root=kk[0]
		i+=1

	print "Case #"+str(pra+1)+": "+str(count)
	pra+=1
