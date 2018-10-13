import sys
input_filename, = sys.argv[1:]
input = open(input_filename)
assert input_filename.endswith('.in'), input_filename
output = open(input_filename[:-3]+'.out', 'w')
    
T = int(input.readline())

def solve():
    S_max, rest = input.readline().strip().split(' ')
    S_max = int(S_max)
    lst = map(int,list(rest))
    assert len(lst) == S_max + 1, 'lst {}, S_max {}'.format(lst, S_max)
    count = 0
    r = 0
    for i, s in enumerate(lst):
        if s > 0:
            a = max(i-count, 0)
        else:
            a = 0
        count += a + s
        r += a
        # print i, s, a, r, count
    return r
        
for t in range(T):
    print >> output, 'Case #%s: %s' % (t+1,solve())
