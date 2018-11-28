def find(a):
	x=int(a[0])
	i=1
	count=0
	while i<len(a):
		if int(a[i])>0 and x<i:
			zz=i-x
			count+=zz
			x+=zz
		x+=int(a[i])
		i+=1
	return count

inp=raw_input().split('\n')
x=int(inp[0])
i=0
while i<x:
    y=inp[i+1]
    y=y.split(' ')[1]
    z=find(y)
    print('case #'+str(i+1)+': '+str(z))
    i+=1
