import sys
from math import log

f = open(sys.argv[1])
f2 = file("out-" + sys.argv[1] + ".txt","w+")
T = int(f.readline())
# T = 500
# T = 1
for t in range(1, T+1):
	N, K = map(int, f.readline().split())
	# N, K = T, t
	# N, K = 500, 500
	stalls = (N, 1, 0)
	
	for i in xrange(int(log(K, 2))):
		# print stalls
		num, cnt, cnt1 = stalls
		if num % 2 == 0:
			stalls = ((num-2)/2, cnt, cnt + cnt1*2)
		else:
			stalls = ((num-1)/2, cnt*2 + cnt1, cnt1)
	# print stalls
	
	remain = K - pow(2, int(log(K, 2))) + 1
	# print remain
	if remain <= stalls[2]:
		res = stalls[0] + 1
	else:
		res = stalls[0]
	if res <= 1:
		res = (0, 0)
	else:
		res = (res/2, (res-1)/2)
	
	res = "%d %d"% res
	
	out = "Case #{0}: {1}".format(t, res)
	print out
	f2.write(out + "\n")
f.close()
f2.close()
