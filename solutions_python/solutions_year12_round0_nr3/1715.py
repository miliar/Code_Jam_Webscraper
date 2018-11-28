inp = file("myfile.in","r")
out = file('outputfile','w')

data = inp.read()

d = data.split('\n')

cases = int(d[0])


def isRever(k,r):
	
	v = str(k)
	val = []

	for i in range(1,len(v)):
		val.append(int(v[i:]+v[:i]))
		if r in val:
			return 1
	return 0

def recPair(a,b):
	

	ans =0
	u = b-a
	k=a
	r=a+9

	for i in range(0 , u +1):
		cnt=1
		while r<=b:

			if isRever(k,r):
				r=r+9*cnt
				ans=ans+1
			else:
				r=r+9*cnt
		
		k=k+1
		r=k+9

	return ans


for i in range(1,cases+1):
	u=recPair( int(d[i].split(" ")[0])  , int(d[i].split(" ")[1]) )
	v='Case #'+str(i)+': '+str(u)
	out.write(v)
	out.write('\n')

inp.close()
out.close()



