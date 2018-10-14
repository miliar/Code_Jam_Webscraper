f = open('magician.in','r')
t = int(f.readline())
for i in range(0,t):
    n = int(f.readline())
    s1 = []
    s2 = []
    for j in range(0,4):
        l = f.readline()
        if j == n-1:
            for s in l.split(' '):
                s1.append(int(s))
    k = int(f.readline())
    for j in range(0,4):
        l = f.readline()
        if j == k-1:
            for s in l.split(' '):
                s2.append(int(s))
    s3 = [val for val in s1 if val in s2]

    if len(s3) == 1:
        print 'Case #%d: %s'%(i+1,int(s3[0]))
    elif len(s3) == 0:
        print 'Case #%d: Volunteer cheated!'%(i+1)
    elif len(s3) > 1:
        print 'Case #%d: Bad magician!'%(i+1)