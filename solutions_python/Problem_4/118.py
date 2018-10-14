f = open('in')
out = open('out','w')

N = int(f.readline())
lines = []
for num in xrange(N):
    d = int(f.readline())
    a = []
    b = []
    for x in xrange(2):
        line = f.readline()
        line = line.split()
        for i in line:
            if x == 0:
                a.append(int(i))
            if x == 1:
                b.append(int(i))
    #=====
    a.sort()
    b.sort()
    b.reverse()
    
    sp = 0
    for i in xrange(d):
        sp += a[i]*b[i]
    
    outLn = 'Case #'+str(num+1)+': '+str(sp)+'\n'
    lines.append(outLn)
out.writelines(lines)