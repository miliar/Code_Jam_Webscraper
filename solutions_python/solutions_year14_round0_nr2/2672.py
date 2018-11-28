import sys

i_file = open(sys.argv[1], 'r')
o_file = open('/home/neeraj/ggle/cookies/cookies_l.out', 'w')

T = int(i_file.readline())
#results = []

def f(l):
	l = [float(i) for i in l.split(' ')]
	return l

def cal_time(n, C, F, X, t):
	t2 = C/(2+(n-1)*F) + t
	curr_time = X/(2+n*F) + t2
	return curr_time, t2

for i in range(T):
	line = f(i_file.readline())
	C, F, X = line[0], line[1], line[2]
	prev_time = X/2.0
	n = 1
	t = 0
	while n:
		curr_time, t = cal_time(n, C, F, X, t)
		if curr_time >= prev_time:
			a = 'Case #' + str(i + 1) + ': ' + str(prev_time) + '\n'
			o_file.write(a)
			break
		n += 1
		prev_time = curr_time

o_file.close()
i_file.close()
		
		
