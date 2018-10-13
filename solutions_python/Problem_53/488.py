import sys
import psyco

def solve(N, K):
	base = 2 ** N
	
	if((K % base) == (base - 1)):
		return "ON"
	else:
		return "OFF"

def main():
	file = open(sys.argv[1])
	
	j = int(file.readline()) + 1
	N = 0
	K = 0
    
	for i in range(1, j):
		N, K = map(int, file.readline().split())
		res = solve(N, K)
		print "Case #%i: %s" % (i, res)

	file.close()

if __name__ == "__main__":
	main()
	
