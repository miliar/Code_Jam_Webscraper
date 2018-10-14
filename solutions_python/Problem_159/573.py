import math
fin = open("in.txt","r")


N = int(fin.readline())


f = open( "out.txt","w")

def first_method(n,m):
	eaten = 0
	for i in range(n-1):
		if m[i+1]<m[i]:
			eaten+= m[i]-m[i+1]
	return eaten

def second_method(n,m):
	eaten = 0
	rate_index = [m[i]-m[i+1] for i in range(n-1)  if m[i+1]<m[i]]
	max_rate = 0
	if rate_index:
		max_rate = max(rate_index)
	for index in range(n-1):
			if m[index] >=max_rate:
				eaten+= max_rate
			else:
				eaten+= m[index]
	return eaten

for T in range(N):
	n = int(fin.readline())
	m = map(int, fin.readline().split())
	y = first_method(n,m)
	z = second_method(n,m)
	f.write("Case #{}: {} {}\n".format(T+1,y,z))

f.close()

fin.close()