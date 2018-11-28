
def solve(A,B,K):
	count = 0
	for a in range(0,A):
		for b in range(0,B):
			if a&b < K:
				count += 1
			
	result = str(count)
	
	return result

	
def main(source, dest):
	fd = open(source, 'r')
	fo = open(dest, 'w')
	T = int(fd.readline())
	for i in range(1,T+1):
		(A,B,K) = fd.readline().split(' ')
		
		result = solve(int(A), int(B), int(K))
	
		print 'Case #' + str(i) + ': ' + result + '\n',
		fo.write('Case #' + str(i) + ': ' + result + '\n')
	
	fd.close()
	fo.close()


if __name__ == "__main__":
	filename = os.path.basename(sys.argv[1])
	source = sys.argv[1]
	dest = os.path.join(sys.argv[2], filename.replace(".in.txt",".out.txt"))
	main(source, dest)