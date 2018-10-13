f = open('A-large.in')
output = open('A-large.out', 'w')

C = int(f.readline())
for c in range(1,C+1):
    ln = f.readline().split()
    ln = map(int, ln)
    P = ln[0]
    K = ln[1]
    L = ln[2]
    freq = f.readline().split()
    freq = map(int, freq)
    f_cpy = [q for q in freq]
    
    keys = []
    for k in range(0,K):
        keys.append([])
    while sum(f_cpy) != (L*-1):
        for k in range(0,K):
            m = max(f_cpy)
            i = f_cpy.index(m)
            f_cpy[i] = -1
            keys[k].append(i)
            if sum(f_cpy) == (L*-1):
                break
    
    output.write('Case #%u: ' % c)
    count = 0
    for l in range(0,L):
        for k in keys:
            if l in k:
                count += (k.index(l) + 1) * freq[l]
    output.write(str(count) + '\n')

f.close()
output.close()
