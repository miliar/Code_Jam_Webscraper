import sys

def main():
	cache = {"1" : {"1" : "1", "i" : "i", "j" : "j", "k" : "k", "-1" : "-1", "-i" : "-i", "-j" : "-j", "-k" : "-k"}, \
	"i" : {"1" : "i", "i" : "-1", "j" : "k", "k" : "-j", "-1" : "-i", "-i" : "1", "-j" : "-k", "-k" : "j"},\
	"j" : {"1" : "j", "i" : "-k", "j" : "-1", "k" : "i", "-1" : "-j", "-i" : "k", "-j" : "1", "-k" : "-i"},\
	"k" : {"1" : "k", "i" : "j", "j" : "-i", "k" : "-1", "-1" : "-k", "-i" : "-j", "-j" : "i", "-k" : "1"},\
	"-1" : {"1" : "-1", "i" : "-i", "j" : "-j", "k" : "-k", "-1" : "1", "-i" : "i", "-j" : "j", "-k" : "k"},\
	"-i" : {"1" : "-i", "i" : "1", "j" : "-k", "k" : "j", "-1" : "i", "-i" : "-1", "-j" : "k", "-k" : "-j"},\
	"-j" : {"1" : "-j", "i" : "k", "j" : "1", "k" : "-i", "-1" : "j", "-i" : "-k", "-j" : "-1", "-k" : "i"},\
	"-k" : {"1" : "-k", "i" : "-j", "j" : "i", "k" : "1", "-1" : "k", "-i" : "j", "-j" : "-i", "-k" : "-1"}
	}

	T = int(sys.stdin.readline())
	c = 1
	while T > 0:
		L, X = map(int, sys.stdin.readline().split())
		ls = sys.stdin.readline()
		ls = ls.rstrip()*X
		
		table = [ '1' for i in xrange(L*X+1) ]
		for i in xrange(L*X):
			table[i+1] = cache[table[i]][ls[i]]
		rOpr = '1'
		res = False
		for r in reversed(xrange(1, L*X+1)):
			if rOpr == 'k':
				for l in xrange(r):
					if table[l] == 'i' and table[r] == 'k':
						res = True
						break
				if res == True:
					break
			rOpr = cache[ls[r-1]][rOpr]
		print 'Case #{0}: '.format(c) + ('YES' if res == True else 'NO')
		
		T -= 1
		c += 1

if __name__ == '__main__':
	main()
