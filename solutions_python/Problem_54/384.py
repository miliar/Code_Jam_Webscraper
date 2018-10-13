def gcd(a,b):
	if b==0:
		return a
	return gcd(b,a%b)

def mod(a):
	if a<0:
		return -1*a;
	return a

sun=input()
pra=1
while pra<=sun: 
	print "Case #"+str(pra)+":",
	l=raw_input()
	ll=l.split(' ')

	x=int(ll[0])
	arr=[]
	i=1
	while i<len(ll):
		y=int(ll[i])
		arr.append(y)
		i+=1

	i=0
	brr=[]
	while i<x:
		j=i+1
		while j<x:
			y=mod(arr[i]-arr[j])
			brr.append(y)
			j+=1
		i+=1

	hcf=brr[0]

	if len(brr)>1:
		hcf=gcd(brr[0],brr[1])

	i=2
	while i<len(brr):
		hcf=gcd(hcf,brr[i])
		i+=1

	#print ' '
	#print "hcf",hcf
	#print "arr[0] ",arr[0]
	if arr[0]%hcf==0:
		print 0
	else:
		print hcf-(arr[0]%hcf)
	pra+=1
