def maxmin(n):
    if n%2 == 0:
        return [n//2, n//2 - 1]
    else:
        return [n//2, n//2]

fread = open('C-large.in')
lines = fread.readlines()
fw = open('output3', 'w')

T = int(lines[0][0:-1])
for t in range(T):
    line = lines[t+1].split(" ")
    N = int(line[0])
    K = int(line[1])

    seq = [] #lista di scelte: 0 per max, 1 per min
    k = K
    newk = K
    i = 0
    while newk>0:
        k = newk
        newk -= 2**i
        i += 1
    i -= 1
    while i>0:
        if k <= 2**(i-1):
            seq.insert(0, 0) #max
        else:
            k -= 2**(i-1)
            seq.insert(0, 1) #min
        i -= 1

    lastmaxmin = maxmin(N)

    for choice in seq:
        lastmaxmin = maxmin(lastmaxmin[choice])

    fw.write('Case #{}: {} {}\n'.format(t+1, lastmaxmin[0], lastmaxmin[1]))
