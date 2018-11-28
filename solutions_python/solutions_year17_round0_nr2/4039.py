def fun(arr):
	if check(arr):
		return arr
	for i in xrange(len(arr)-1,0,-1):
		if arr[i]<arr[i-1]:
			if arr[i]=='0':
				p = int(''.join(arr))-10**(len(arr)-1-i)
				arr = list(str(p))
				for t in xrange(len(arr)-1,i-1,-1):
					arr[t]='9'
			else:
				arr[i-1] = str(int(arr[i-1])-1)
				for k in xrange(len(arr)-1,i-1,-1):
					arr[k] = '9'
	return fun(arr)

def check(arr):
	for i in xrange(len(arr)-1,0,-1):
		if int(arr[i])<int(arr[i-1]):
			return False
	return True

total = 0
f = open('ap1.txt','r')
n=0
last = 0
g = open('large.txt','w')
for l in f:
	if total==0:
		total+=1
		n = int(l)
		continue
	number = int(l)
	last = 0
	arr = list(str(number))
	arr = fun(arr)
	last = int(''.join(arr))
	g.write("Case #"+str(total)+": "+str(last)+"\n")
	total+=1

g.close()