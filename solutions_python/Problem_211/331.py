import numpy as np

def fill(l, U):
	l = sorted(l)
	while U > 0:
		cur = 0
		diff = 0
		while cur < len(l)-1:
			diff = l[cur+1] - l[cur]
			if diff > 0:
				break;
			else:
				cur = cur + 1

		if diff == 0:
			l = [l[0] + (U / (cur+1))]*(cur+1)
			return l

		if U > (cur+1) * diff:
			l[0:cur+1] = [l[cur+1]]*(cur+1)
			U = U - (cur+1) * diff
		else:
			inc = U / (cur+1)
			U = 0
			l[0:cur+1] = [l[cur] + inc]*(cur+1)

	return l



f_out = open('C-small-1-attempt1.out', 'w')
with open('C-small-1-attempt1.in') as f_in:
	T = int(f_in.readline())
	for i in xrange(T):
		N, K = f_in.readline().split(' ')
		N = int(N)
		K = int(K)
		U = float(f_in.readline())
		l = f_in.readline().split(' ')
		l = [float(x) for x in l]


		p_out = np.prod(fill(l, U))
		f_out.write('Case #' + str(i+1) + ': ' + str(p_out) + '\n')


