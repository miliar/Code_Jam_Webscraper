import sys

def main():
	file = open(sys.argv[1], 'r')
	C = int(file.readline().rstrip())
	for i in range(C):
		s = file.readline().rstrip()
		n = int(s[0])
		have = 0
		need = 0
		for j in range(n+1):
			if have + need < j:
				need += j-have-need
			have += int(s[2+j])
		print 'Case #{0}: {1}'.format(i+1, need)
		
if __name__ == '__main__':
	main()