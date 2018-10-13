import sys
stdin = sys.stdin
ncases = int(stdin.readline())

for ncase in range(ncases):
    N, P = map(int, stdin.readline().strip().split(' '))

    count = 0
    gs = {0: 0, 1: 0, 2: 0, 3: 0}
    vals = map(int, stdin.readline().strip().split(' '))
    for val in vals:
        gs[val % P] += 1

    def take(ls):
        c = 0
        complete = False
        while not complete:
            for a in ls:
                gs[a] -= 1
                if gs[a] < 0:
                    complete = True
            if not complete:
                c += 1
        for a in ls:
            gs[a] += 1
        return c

    count += take([0])
    if P == 2:
        count += take([1, 1])
    elif P == 3:
        count += take([1, 2])
        count += take([1, 1, 1])
        count += take([2, 2, 2])
    elif P == 4:
        count += take([2, 2])
        count += take([1, 3])
        count += take([1, 1, 2])
        count += take([2, 3, 3])
        count += take([1, 1, 3, 3])
        count += take([1, 1, 1, 1])
        count += take([3, 3, 3, 3])
    
    any_left = gs[1] > 0 or gs[2] > 0 or gs[3] > 0
    if any_left:
        count += 1

    print('Case #{0}: {1}'.format(ncase + 1, count))