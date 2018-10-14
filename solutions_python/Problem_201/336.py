import sys

sys.stdin = open('in.txt', 'r+')
sys.stdout = open('out.txt', 'w+')

def get_height(t):
	h = 1 
	while t > 1:
		h += 1
		t = t // 2

	return h

TC = int(input())
for _ in xrange(1, TC+1):
	n, k  = map(int, raw_input().split())

	h = get_height(k)
	s = n - (2**(h-1)-1)
	m = 2**(h-1)

	k -= (2**(h-1)-1)

	res = s // m

	if s % m >= k:
		res += 1

	# print(s, m, k, h, res)

	print("Case #{0}: {1} {2}".format(_, (res)//2, (res-1)//2))