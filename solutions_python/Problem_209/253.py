import math

f= open('A-large.in')
T = int(f.readline())
for i in range(T):
    l = f.readline()
    N = int(l.split()[0])
    K = int(l.split()[1])
    pancakes = []
    for n in range(N):
        l = f.readline()
        r = int(l.split()[0])
        h = int(l.split()[1])
        pancakes.append([r,h,r*h])
    pancakes = sorted(pancakes,key = lambda x:x[0])
    subset = []
    sumArea = 0
    for n in range(K):
        subset.append(pancakes[n])
        sumArea += 2 * math.pi * pancakes[n][2]
    maxR = subset[-1][0]
    for n in range(K,N):
        subset = sorted(subset,key = lambda x:x[2])
        if pancakes[n][0]*pancakes[n][0] + 2*pancakes[n][2] > maxR*maxR + 2*subset[0][2]:
            sumArea -= 2 * math.pi * subset[0][2]
            del subset[0]
            subset.append(pancakes[n])
            sumArea += 2 * math.pi * subset[-1][2]
            maxR = pancakes[n][0]
        #print subset
    sumArea += math.pi * maxR * maxR
    print 'Case #%d: %f' % (i+1,sumArea)
        
    