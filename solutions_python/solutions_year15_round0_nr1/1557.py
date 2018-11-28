import sys

def minspec(reference):
	risen = 0
	friends = 0
	for i in range(len(reference)):
		if (risen + friends >= i):
			risen += int(reference[i])
		else:
			while(risen + friends != i):
				friends += 1
			risen += int(reference[i])
	return friends

def main():
	cases = int(sys.stdin.readline())
	for i in range(cases):
		param = sys.stdin.next().split()
		param[0] = int(param[0])
		print "Case #%d:" % (i+1),minspec(param[1])
	sys.stdout.flush()

if __name__ == '__main__':
	main()