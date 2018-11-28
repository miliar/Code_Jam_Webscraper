import math
ncases = int(raw_input().strip())
memo_fas = {}
memo_pal = {}

is_pal = lambda x: str(x) == str(x)[::-1]

def is_valid_for_fas(num):
	global memo_pal, memo_fas
	if not memo_fas.has_key(num):
		memo_fas[num] = is_pal(num) and is_pal(num*num)

	return memo_fas[num]

case_i = 0
for case_i in range(ncases):
	f, t = raw_input().strip().split(' ')
	f = int(f)
	t = int(t)
	f_rt = math.sqrt(f)
	t_rt = math.sqrt(t)
	n_fs = 0

	for i in range( int(math.floor(f_rt)) , int(math.ceil(t_rt))+1  ):
		if i < f_rt:
			continue

		if is_valid_for_fas(i) and f <= i*i <= t:
			#print "FAS", i
			n_fs += 1

	print "Case #%d: %d" % (case_i+1,n_fs)