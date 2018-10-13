def count_mkdirs(curdir, path):
    count = 0
    root = curdir
    for direc in path.split('/')[1:]:
        if direc not in curdir:
            curdir[direc] = {}
            count += 1
        curdir = curdir[direc]
        
    return root, count

##root = {}
##root, count = count_mkdirs(root, '/home/foo/bar')
##print count
##root, count = count_mkdirs(root, '/home/foo/baz')
##print count

def depth(path):
    return path.count('/')

def read_input(n, m):
    existing = []
    new = []
    for i in xrange(n):
        existing_dir = raw_input()
        existing.append(existing_dir)
        
    for i in xrange(m):
        new_dir = raw_input()
        new.append((new_dir, depth(new_dir)))
        
    new.sort(key=lambda node: node[1])
    
    new2 = [newe[0] for newe in new]
    return existing, new2

def calculate(existing, new, case):
    root = {}    
    
    for direc in existing:
        root, count = count_mkdirs(root, direc)
        
    count = 0
    
    for new_dir in new:
        root, add_count = count_mkdirs(root, new_dir)
        count += add_count
        
    return count

for case_number in xrange(int(raw_input())):
    n, m = map(int, raw_input().split())
    existing, new = read_input(n, m)
    result = calculate(existing, new, str(case_number))
    print 'Case #%d: %s' % (case_number+1, result)