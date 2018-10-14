from itertools import combinations

def trans(pan):
    ls2 = []
    for x in list(pan):
        if x == '+':
            ls2.append(1)
        else:
            ls2.append(0)
    return ls2


def flip(pan, i, k):
    for i in range(i, i+k):
        pan[i] = (pan[i]+1)%2


def sim(pan, k):
    n = len(pan)
    if sum(pan) == n:
        return '0'
    ind = range(n-k+1)
    for j in range(1, n-k+1 +1 ):
        for case in combinations(ind, j):
            pan2 = list(pan)
            for i in case:
                flip(pan2, i, k)
            if sum(pan2) == n:
                return str(j)
    return 'IMPOSSIBLE'


with open('A-small-attempt1.in', 'r') as f:
    with open('q1solution.txt', 'w') as solution:
        t = int(f.readline())
        for case in range(t):
            n = f.readline().split()
            pan = trans(n[0])
            k = int(n[1])
            sol = sim(pan, k)
            solution.write('Case #' + str(case+1) + ': ' + sol + '\n')