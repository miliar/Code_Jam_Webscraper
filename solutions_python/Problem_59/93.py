import sys

f = open('A-large.in')

t = int(f.readline().strip())

for case in range(t):
    n, m = map(int, f.readline().strip().split(' '))
    
    root = {}
    
    for i in range(n):
        s = f.readline().strip().strip('/').split('/')
        cwd = root
        for dir in s:
            if not cwd.has_key(dir):
                cwd[dir] = {}
            cwd = cwd[dir]
        # print s
    # print root
        
    res = 0
    for i in range(m):
        s = f.readline().strip().strip('/').split('/')
        
        cwd = root
        for dir in s:
            if not cwd.has_key(dir):
                cwd[dir] = {}
                res += 1
                # print 'create', dir
            cwd = cwd[dir]
            
    print 'Case #%d: %d' % (case+1, res)