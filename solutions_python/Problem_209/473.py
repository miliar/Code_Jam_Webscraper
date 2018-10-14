# Google Code Jam 2017 Round 1C
# Problem A. Ample Syrup

from math import pi

def pancakes(N, K, R, H):
    possible = 0
    for i in range(N):
        current = R[i]
        above = []
        new = 0
        able = True
        if K != 1:
            for j in range(N):
                if j != i and R[j] <= current:
                    above += [2*pi*R[j]*H[j]]
            if len(above) >= K - 1:
                new = sum(sorted(above)[::-1][:K - 1])
            else:
                able = False
        if able:
            new += pi*current**2 + 2*pi*current*H[i]
            if new > possible:
                possible = new
    return possible

def piles():
    f = open('syrup.txt', 'r')
    g = open('pancakes.txt', 'w')
    line = 0
    part = 0
    for i in f:
        if line == 0:
            T = int(i)
            line = 1
        else:
            if part == 0:
                N = ''
                K = ''
                space = False
                for j in i:
                    if j == ' ':
                        space = True
                    else:
                        if space:
                            if j != '\n':
                                K += j
                        else:
                            N += j
                N = int(N)
                K = int(K)
                R = []
                H = []
                part = 1
            else:
                first = ''
                second = ''
                space = False
                for j in i:
                    if j == ' ':
                        space = True
                    else:
                        if space:
                            if j != '\n':
                                second += j
                        else:
                            first += j
                R += [int(first)]
                H += [int(second)]
                if len(R) == N:
                    g.write('Case #' + str(line) + ': ')
                    g.write(str(pancakes(N, K, R, H)))
                    g.write((T != line)*'\n')
                    part = 0
                    line += 1
                    print line
    f.close()
    g.close()
