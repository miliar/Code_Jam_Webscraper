from bisect import bisect

f = open('A-large.in')
lines = f.read().splitlines()
f.close()

T = int(lines.pop(0))
results = []

        
for k in xrange(T):
    N, M = [int(x) for x in lines.pop(0).split()]
    
    #Keep a sorted list of directories
    paths = []
    for n in xrange(N):
        path = lines.pop(0)
        index = bisect(paths, path)
        paths.insert(index, path)
    
    mkdirs = 0
    for m in xrange(M):
        path = lines.pop(0)
        if path not in paths:
            #Parse until we get to lowest level
            dirs = path.split('/')
            temp = ['']
            dirs.pop(0) #We don't need the root
            for d in dirs:
                temp.append(d)
                s = '/'.join(temp)
                if s not in paths:
                    mkdirs+=1
                    paths.append(s)
                    
    results.append('Case #%d: %s' % (k+1,mkdirs))

f = open('A-large.out','w')
f.write('\n'.join(results)+'\n')
f.close()

#print '\n'.join(results)+'\n'
