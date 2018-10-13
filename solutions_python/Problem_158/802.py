def solve(X, R, C):
	if X == 1:
		return "GABRIEL"
	if X == 2:
		return "GABRIEL" if R*C%2==0 else "RICHARD"
	if X == 3:
		return "RICHARD" if R == 1 or C == 1 or R*C%3 != 0 else "GABRIEL"
	if X == 4:
		return "GABRIEL" if (R*C==12) or (R*C==16) else "RICHARD"

	
def main(source, dest):
	fd = open(source, 'r')
	fo = open(dest, 'w')
	T = int(fd.readline())
	for i in range(1,T+1):
		(X, R, C) = fd.readline().split(' ')
		result = solve(int(X), int(R), int(C))
	
		print 'Case #' + str(i) + ': ' + result + '\n',
		fo.write('Case #' + str(i) + ': ' + result + '\n')
	
	fd.close()
	fo.close()


if __name__ == "__main__":
	filename = os.path.basename(sys.argv[1])
	source = sys.argv[1]
	dest = os.path.join(sys.argv[2], filename.replace(".in.txt",".out.txt"))
	main(source, dest)