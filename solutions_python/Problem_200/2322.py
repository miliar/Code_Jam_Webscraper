# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
def find_tidy_num(N, prefix="", m=0): 
    num_digs = len(str(N))-len(prefix)
    if num_digs == 0:
        return ""
    curr_best = str(m)
    while int(curr_best) < 9 and int(prefix + str(int(curr_best)+1)*num_digs) <= N:
        curr_best = str(int(curr_best)+1)
    return curr_best + find_tidy_num(N, prefix + curr_best, curr_best)

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    N = int(raw_input())
    print "Case #{}: {}".format(i, int(find_tidy_num(N)))
