import sys

def isSorted(N):
	return str(N) == ''.join(sorted(str(N)))
	
f = open(sys.argv[1])
f2 = file("out-" + sys.argv[1] + ".txt","w+")
T = int(f.readline())
for t in range(1, T+1):
	N = f.readline().strip('\n')
	
	while(isSorted(N) == False):
		res = int(N[:2]) - 1
		while(isSorted(res) == False):
			res -= 1
		# print N, (len(N)-2)
		N = str(res) + "9"*(len(N)-2)
	res = N
	
	out = "Case #{0}: {1}".format(t, res)
	print out
	f2.write(out + "\n")
f.close()
f2.close()
