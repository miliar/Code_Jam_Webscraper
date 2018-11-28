#import math

def solve(Smax, S):
	standing=0
	extras = 0
	i = 0
	for i in range(Smax+1):
		if standing < i:
			extras += i-standing
			standing = i
		standing += S[i]
	return "%d"%extras
	
def main(source, dest):
	fd = open(source, 'r')
	fo = open(dest, 'w')
	T = int(fd.readline())
	for i in range(1,T+1):
		linebits = fd.readline().rstrip().split(' ')
		Smax = int(linebits[0])
		S = [int(c) for c in linebits[1]]
		result = solve(Smax, S)
	
		print 'Case #' + str(i) + ': ' + result + '\n',
		fo.write('Case #' + str(i) + ': ' + result + '\n')
	
	fd.close()
	fo.close()


if __name__ == "__main__":
	filename = os.path.basename(sys.argv[1])
	source = sys.argv[1]
	dest = os.path.join(sys.argv[2], filename.replace(".in.txt",".out.txt"))
	main(source, dest)