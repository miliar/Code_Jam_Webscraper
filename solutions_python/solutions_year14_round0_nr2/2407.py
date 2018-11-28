import sys
rl = lambda : sys.stdin.readline().strip()

def solve( C, F, X ):
	best = 1e+1000
	elapsed = 0.0
	perCookie = 2
	while elapsed <= best:
		best = min( best, elapsed + X / perCookie )	
		elapsed += C / perCookie
		perCookie += F	

	return best

def main():
	ncase = int( rl() )
	for caseno in xrange(1,ncase+1):
		C, F, X = map( float, rl().split() )
		print "Case #%d: %.9f " % ( caseno, solve(C,F,X) )

if __name__ == "__main__":
	main()
