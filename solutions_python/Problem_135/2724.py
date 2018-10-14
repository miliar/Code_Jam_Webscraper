'''
Created on 12-Apr-2014

@author: raju
'''
with open('/home/raju/Downloads/A-small-attempt1.in') as f:
    t = int(f.readline())
    for i in xrange(t):
        r1 = int(f.readline())
        a = [[0 for x in xrange(4)] for x in xrange(4)] 
        for j in xrange(4):
            l1 = set(int(x) for x in f.readline().split())
            a[j] = l1
        r2 = int(f.readline())
        b = [[0 for x in xrange(4)] for x in xrange(4)]
        for j in xrange(4):
            b[j] = set(int(x) for x in f.readline().split())
        s = a[r1-1].intersection(b[r2-1])
        if not s:
            print 'case #'+str(i+1)+': Volunteer cheated!'
            continue
        if len(s) == 1:
            print 'case #'+str(i+1)+': ' + str(next(iter(s)))
            continue
        else:
            print 'case #'+str(i+1)+': Bad magician!'
        