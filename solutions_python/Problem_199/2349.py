import sys

f = open(sys.argv[1])
f2 = file("out-" + sys.argv[1] + ".txt","w+")
T = int(f.readline())
for t in range(1, T+1):
	S, K = f.readline().split()
	S = [True if s == "+" else False for s in S]
	K = int(K)
	# print S
	res = 0
	
	while(False in S):
		i = S.index(False)
		if(i+K > len(S)):
			res = "IMPOSSIBLE"
			break
		S[i:i+K] = [not s for s in S[i:i+K]]
		# print i, S
		res += 1
		
	out = "Case #{0}: {1}".format(t, res)
	print out
	f2.write(out + "\n")
f.close()
f2.close()
