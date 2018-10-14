afile = open('A.in','r')
numTestCase = int(afile.readline())

outfile = open('A.out','w')

for _i in range(1, numTestCase + 1):
    n = int(afile.readline().strip('\n'))
    
    l = []
    for _ii in range(0,n):
        s1 = afile.readline().strip('\n')
        a, b = map(int, s1.split(' '))
        l.append([a,b])

    count = 0
    for w1 in l:
        for w2 in l:
            if w1[0] - w2[0] == 0:
                continue
            if w1[0] - w2[0] > 0 and w1[1] - w2[1] > 0:
                continue
            if w1[0] - w2[0] < 0 and w1[1] - w2[1] < 0:
                continue
            
            count += 1
            
    outfile.write('Case #{0}: {1}\n'.format(_i, count//2))
    
afile.close()    
outfile.close()    