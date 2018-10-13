import math
fout = open('osmos.ans.txt', 'w')
fin = open ('A-small-attempt1.in', 'r')

def inc(numb):
    return numb + numb - 1

T = int(fin.readline())
for i in range(T):
    A, N = map(int, fin.readline().split())
    sizes = map(int, fin.readline().split())
    sizes.sort();
    print sizes;
    steps = 0
    for j in range (N):
        tempsteps = 0
        stop = False
        while A <= sizes[j]:
            A = inc(A)
            tempsteps += 1
            if tempsteps >= N - j:
                stop = True
                break
        A += sizes[j]
        if stop:
            steps += N - j
            break
        else:
            steps += tempsteps
    fout.write('Case #' + str(i+1) + ': ' + str(steps) + '\n')

fin.close()
fout.close()
        
