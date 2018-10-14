import sys

def min_flip(s, k):
	count = 0
	s = list(s)
	for i in range(len(s)):
		if(s[i] == '-'):
			if (len(s) - i) < k:
				return -1

			count += 1
			for j in range(k):
				if s[i+j] == '-':
					s[i+j] = '+'
				else:
					s[i+j] = '-'

	return count

if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)

    t = int(f.readline())
    for i in xrange(t):
    	s, k = f.readline().split()
    	k = int(k)
    	count = min_flip(s,k)
    	if(count < 0):
    		print("CASE #{0}: IMPOSSIBLE".format(i+1))
    	else:
    		print("CASE #{0}: {1}".format(i+1, count))

