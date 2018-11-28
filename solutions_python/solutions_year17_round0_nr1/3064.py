def flip(array, pos, K):
    for q in range(pos, pos + K):
        array[q] = not array[q]

fi = open('A-large.in', 'r')
fo = open('outputA-large.txt', 'w')

T = int(fi.readline())

for t in range(T):

    linetok = fi.readline().split()
    line = linetok[0]
    K = int(linetok[1])
    N = len(line)
    lineB = [False] * N
    
    for i in range(N):
        if line[i] == '+':
            lineB[i] = True
            
    steps = 0
    finished = False
    impossible = False
    p = 0

    while finished == False:
        if lineB == [True] * N:
            finished = True
            break
        if p > N - K:
            impossible = True
            finished = True
            break
        if lineB[p]:
            p += 1
        else:
            flip(lineB, p, K)
            steps += 1
            p += 1
    
    if impossible:
        fo.write('Case #{0}: IMPOSSIBLE\n'.format(t+1))
    else:
        fo.write('Case #{0}: {1}\n'.format(t+1, steps))
    
fi.close()
fo.close()
