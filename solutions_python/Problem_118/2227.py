from math import sqrt

def is_pal(x):
	return str(x) == str(x)[::-1]

def main(t):
	A,B = input().split()
	A,B = int(A),int(B)
	c = 0
	for x in range(A,B+1):
			y = sqrt(x)
			if y.is_integer():
				y = int(y)
				if is_pal(y) and is_pal(x):
					c += 1
	print("Case #{0}: {1}".format(t+1,c))

Nt = int(input())
for t in range(Nt):
	main(t)
