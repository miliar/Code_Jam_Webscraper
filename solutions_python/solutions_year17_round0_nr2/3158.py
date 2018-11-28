from sys import argv
with open(argv[1]) as infile:
	T = int(infile.readline().strip())
	for i in range(T):
		N = int(infile.readline())
		l = list(map(int, list(str(N))))
		j = len(l)-1
		while j> 0 and sorted(l)!=l:
			if max(l[:j]) > l[j]:
				l[j:] = [9]*(len(l)-j)
				l[j-1] -= 1
			j -= 1
		n = int(''.join(str(x) for x in l))
		print "Case #"+str(i+1)+":", n
