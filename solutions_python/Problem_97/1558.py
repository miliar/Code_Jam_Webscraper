import sys

def find_recycled(n, m):
    recycled = set()
    n_str = str(n)
    x = n_str[-1:] + n_str[:-1]
    
    
    for i in range(len(n_str)-1):
        tmp = int(x)
        if tmp > n and tmp <= m:
            recycled.add((n,tmp))
            
        x = x[-1:] + x[:-1]
    
    return recycled


result_tmpl = "Case #%d: %d"

f = sys.stdin
lines = int(f.readline())

for i in xrange(lines):
    a,b = map(int, f.readline().split(' '))
    recycled = set()
    for n in xrange(a,b):
        recycled.update(find_recycled(n, b))
                
    print result_tmpl % (i+1, len(recycled))