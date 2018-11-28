
def solve(cas):
	n, s = raw_input().split()
	n    = int(n)
	a    = map(int,s)
	cnt  = 0
	ans  = 0
	for i in xrange(n+1):
		if a[i]>0:
			if cnt<i:
				ans += i-cnt
				cnt  = i
			cnt += a[i]
	print "Case #%d: %d" % (cas,ans)

def main():
	T = int(raw_input())
	for tc in xrange(T):
		solve(tc+1)

main()
