T = int(raw_input())

def doprob():
	N, K = map(int, raw_input().split())
	tmp = len(bin(K)) - 2
	abv = (2**(tmp-1))-1
	num = (N - abv)/(2**(tmp-1))
	if (N - abv) % (2**(tmp-1)) >= K - abv:
		num += 1
	if num % 2 == 0:
		return str(num/2)+" "+str(num/2-1)
	else:
		return str((num-1)/2)+" "+str((num-1)/2)

for qq in xrange(T):
	print "Case #" + str(qq+1) + ": " + str(doprob())