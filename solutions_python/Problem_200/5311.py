import copy
def tidy(n):
	m=copy.deepcopy(n)
	m.sort()
	return m==n

def blow(n):
	i = n
	while i!=0:
		z = [int(x) for x in str(i)]
		if tidy(z):
			return i
		else:
			i-=1



if __name__ == '__main__':
	t = int(input())
	for i in range(t):
		x = int(raw_input())
		res = blow(x)
		print "Case #" + str(i+1) + ": " + str(res)