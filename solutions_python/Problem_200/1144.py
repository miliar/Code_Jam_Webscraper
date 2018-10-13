import sys

f_in, f_out = None, None

def solve():
	global f_in, f_out
	N = f_in.readline().split()[0]
	sn = map(int, N)
	for k in xrange(len(sn)):
		for i in xrange(len(sn)-1):
			if sn[i] > sn[i+1]:
				sn[i] -= 1
				for j in xrange(i+1, len(sn)):
					sn[j] = 9
				break
	new_n = map(str, sn)
	if new_n[0] == '0':
		new_n = new_n[1:]
	return "".join(new_n)
			

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
    


