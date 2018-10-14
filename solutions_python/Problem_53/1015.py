import sys

def cf(case,n,k):

	matrix = []

	for i in xrange(0,n): matrix.append([-1]*k)

	def f(n,k):
		if(k == 0 and n > 0): return False
		elif (n == 0):
			return (((k+1) % 2) == 1)
		else:	
			precomp = matrix[n][k]
			if precomp != -1: return precomp
			else:
				res = True
				for i in xrange(0,n):
					res = res and f(i,k - 1)
				toreturn = f(n,k - 1)
				if res: toreturn = toreturn ^ True 
				matrix[n][k] = toreturn
				return toreturn

	if k == 0:
		return ("Case #%d: OFF\n" % case)
	else:
		result = True
		for i in xrange(0,n): result = result and f(i,k-1)

		if result: return ("Case #%d: ON\n" % case)
		else: return ("Case #%d: OFF\n" % case)

t = sys.stdin.readline()

output = ""

for i in xrange(1,int(t)+1):
	n,k = sys.stdin.readline().strip().split(" ")
	output = output + cf(i,int(n),int(k))

print output
