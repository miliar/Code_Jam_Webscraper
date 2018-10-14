#f = file(r'practice.txt', 'rt')
#out = file(r'practice.out', 'w+t')
#f = file(r'A-small.in', 'rt')
#out = file(r'A-small.out', 'w+t')
f = file(r'A-large.in', 'rt')
out = file(r'A-large.out', 'w+t')

def add_and_count(dirs, d):
    if d in dirs:
        return (dirs, 0)
    if d == '':
        return (dirs, 0)
    dirs.add(d)
    (dirs, c) = add_and_count(dirs, d[:d.rindex('/')])
    return (dirs, c+1)

t=int(f.readline())

for i in xrange(t):
    dirs=set()
    (n, m) = map(int, (f.readline().split()))
    print n,m
    for j in xrange(n):
        d = f.readline().strip()
        (dirs, count) = add_and_count(dirs, d)
        #d = f.readline().split('/')
        #ld = ''
        #for k in xrange(len(d)):
        #    ld = ld+'/'+d[k]
        #    dirs.append(ld)
    print dirs
    count = 0
    for j in xrange(m):
        d = f.readline().strip()
        (dirs, c) = add_and_count(dirs, d)
        count = count + c
    
    out.write('Case #%d: %s\n' % (i+1, count))
f.close()
out.close()
print 'Done!'