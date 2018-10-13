f_in = open('in.txt', 'r')
f_out = open('out.txt', 'w')

T = int(f_in.readline().split()[0])

def func(pairs, N):
    pairs.sort()
    intersection = 0
    for i in xrange(N):
        x=pairs[i]
        for j in xrange(i+1, N):
            if pairs[j][1] < x[1]:
                intersection+=1
    return intersection

for i in xrange(T):
    pairs = []
    N = int(f_in.readline().split()[0])
    for ii in xrange(N):
        pair = f_in.readline().split()
        pairs.append((int(pair[0]), int(pair[1])))
    result = func(pairs, N)
    f_out.writelines('Case #%d: %d\n' % (i+1, result))
        
        
        
