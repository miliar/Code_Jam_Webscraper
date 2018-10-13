def main():
	[D,N] = map(int,raw_input().split())
	time = 0
	for j in xrange(N):
		[K,S] = map(float,raw_input().split())
		T = (D-K)/S
		time = max(T,time)
	return D/time

T = input()
for i in range(T):
	res = main()
	print "Case #" + str(i+1) + ":","{:.9f}".format(res)
