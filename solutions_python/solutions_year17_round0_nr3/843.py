import bisect

def fill(N, K):
	l = 0
	K_temp = K
	while K_temp != 0:
		K_temp = K_temp >> 1
		l = l + 1

	d = 2**(l-1)
	space = (N-d+1) / d 
	num_more = (N-d+1) % d
	if (K-d+1) <= num_more:
		space = space + 1
	return (space-1)-(space-1)/2, (space-1)/2

f_out = open('C-large.out', 'w')
with open('C-large.in') as f_in:
	T = int(f_in.readline())
	for i in xrange(T):
		N, K = f_in.readline().split(' ')
		N = int(N)
		K = int(K)
		f_out.write('Case #' + str(i+1) + ': ')
		right, left = fill(N, K)
		f_out.write(str(right) + ' ' + str(left) + '\n')

