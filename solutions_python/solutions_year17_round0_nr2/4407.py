f = open("in2.txt",'r')

def blah(n):
	k = 0
	for i in range(len(n)):
		if n[i] < k:
			n[i-1] = n[i-1] - 1
			k = n[i-1]
			for j in range(i-2,-1,-1):
				if n[j] <= k:
					for a in range(j+2,len(n)):
						n[a] = 9
					return n
				n[j] = n[j] - 1
				k = n[j] - 1
			for a in range(1,len(n)):
				n[a] = 9
			return n
		k = n[i]
	return n

T = int(f.readline())
for t in range(T):
	N = int(f.readline())
	n = []
	while N > 0:
		n.append(N%10)
		N = N/10
	n = n[::-1]
	n = blah(n)[::-1]
	mult = 1
	num = 0
	for i in range(len(n)):
		num = num + n[i]*mult
		mult = mult*10
	
	print("Case #" + str(t+1) + ": " + str(num))
	
