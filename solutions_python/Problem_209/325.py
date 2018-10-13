import math

def stack(pancake,k):
	n = len(pancake)
	pancake = sorted(pancake, reverse=True, key=lambda k: [k[0], k[1]])
	circ = [None]*n
	for i in range(n):
		circ[i] = 2*math.pi*pancake[i][0]*pancake[i][1]

	area = [None]*(n-k+1)
	for i in range(n-k+1):
		top = math.pi*(pancake[i][0]**2)
		temp = sorted(circ[i+1:n], reverse=True)
		side = circ[i] + sum(temp[0:k-1])
		area[i] = top + side
		
	return max(area)


print stack([[9,3],[7,1],[10,1],[8,4]],2)


## I/O Handler
fIn = open('A_1.txt', 'r')
fOut = open('A_1_sol.txt','w+')
nCases = int(fIn.readline())
for i in range(nCases):
	t = fIn.readline()
 	n, k = t.split(" ")
 	n = int(n)
 	k = int(k)
 	pancake = [[None,None] for j in range(n)] # Initialize 
 	for j in range(n):
 		t = fIn.readline()
 		r, h = t.split(" ")
 		pancake[j][0] = int(r)
 		pancake[j][1] = int(h)
 	ans = stack(pancake,k)
 	output = "Case #{}: {}\n".format(i+1,ans)
 	fOut.write(output)
fIn.close
fOut.close


