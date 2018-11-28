import sys

f_in, f_out = None, None

def solve():
	global f_in, f_out
	n,k = map(int, f_in.readline().split())
	cnt_small, cnt_big = 0,1
	n_small, n_big = 0, n
	i = 1
	while 2**i <= k:
		new_n_small = n_big / 2 - 1
		new_n_big = n_big / 2
		if n_big % 2 == 0:
			if new_n_small == 0:
				new_cnt_small = 0
			else:
				new_cnt_small = 2*cnt_small + cnt_big
			new_cnt_big = cnt_big
		else:
			if new_n_small == 0:
				new_cnt_small = 0
			else:
				new_cnt_small = cnt_small
			new_cnt_big = cnt_small + 2*cnt_big
		
		n_small, n_big = new_n_small, new_n_big
		cnt_small, cnt_big = new_cnt_small, new_cnt_big
		i+=1
	
	if k - 2**(i-1) < cnt_big:
		if n_big % 2 == 0:
			a, b = n_big / 2 - 1, n_big / 2
		else:
			a, b = n_big / 2, n_big / 2
	else:
		if n_small % 2 == 0:
			a, b = n_small / 2 - 1, n_small / 2
		else:
			a, b = n_small / 2, n_small / 2
	return "{0} {1}".format(b,a)
			

def open_file_and_create_output_file(fn_in):
    global f_in, f_out
    dot_idx = fn_in.rfind('.')
    if dot_idx == -1:
        fn_out = fn_in + '.out'
    else:
        fn_out = fn_in[:dot_idx] + '.out'
    
    f_in = open(fn_in, 'rb')
    f_out = open(fn_out, 'wb')
    
def main(filename):
    global f_in, f_out
    open_file_and_create_output_file(filename)

    T = int(f_in.readline())

    for t in xrange(1, T+1):
        ans = solve()
        f_out.write('Case #{0}: {1}\n'.format(t, ans))
    
    f_in.close()
    f_out.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Usage: {0} <input_file>".format(sys.argv[0])
    main(sys.argv[1])
    


