import math
def is_square(n):
    return math.sqrt(n).is_integer()

f = open("input.in","r")
out = open("output.txt","w")
arr = f.readlines()
cases = int(arr[0][:-1])
arr.pop(0)
for i in xrange(0,cases-1):
	arr[i] = arr[i][:-1]
for i in xrange(0,cases):
	cred = arr[i].split(" ")
	minm = int(cred[0])
	maxm = int(cred[1])
	count = 0
	filtered = []
	sqrtmin = int(math.ceil(math.sqrt(minm)))
	sqrtmax = int(math.floor(math.sqrt(maxm)))

	'''while(1):
		if is_square(minm):
			filtered.append(minm)
		minm+=1
		if minm+1==maxm+2:
			break
	'''
	for j in xrange(sqrtmin,sqrtmax+1):
		if str(j) == str(j)[::-1]:
			if str(j*j) == str(j*j)[::-1]:
				count +=1 						
	out.write("Case #"+str(i+1)+": "+str(count)+"\n")