import sys
from collections import Counter
import copy

def a(ctickets):
    rides = 0
    promotions = 0
    while True:
        if len(ctickets[0]) == 0:
            rides += len(ctickets[1])
            break
        elif len(ctickets[1]) == 0:
            rides += len(ctickets[0])
            break
        rides += 1

        if ctickets[0][0] != ctickets[1][-1]:
            # both can ride without promotion
            ctickets[0].pop(0)
            ctickets[1].pop(-1)
        elif ctickets[0][0] != ctickets[1][0]:
            # both can ride without promotion
            ctickets[0].pop(0)
            ctickets[1].pop(0)
        else:
            if ctickets[0][0] == 1:
                # both want the front seat
                ctickets[0].pop(0)
            else:
                ctickets[0].pop(0)
                ctickets[1].pop(-1)
                promotions += 1
    return rides, promotions

def b(ctickets):
    rides = 0
    promotions = 0
    remaingtickets = True
    while True:
        if len(ctickets[0]) == 0:
            rides += len(ctickets[1])
            break
        elif len(ctickets[1]) == 0:
            rides += len(ctickets[0])
            break
        rides += 1

        x = ctickets[0].pop(0)
        for i in range(len(ctickets[1])):
            if x != ctickets[1][i]:
                ctickets[1].pop(i)
                break
        else:
            if x != 1:
                promotions += 1
                ctickets[1].pop()

    return rides, promotions

def solve(N, C, tickets):
    assert(C == 2)
    ctickets = [ [] for x in range(C) ]
    for t in tickets:
        ctickets[t[1]-1].append(t[0])
    for i in range(len(ctickets)):
        ctickets[i] = sorted(ctickets[i])
    rides, promotions = min(a(copy.deepcopy(ctickets)), b(copy.deepcopy(ctickets)))
    #print('a', a(copy.deepcopy(ctickets)))
    #print('b', b(copy.deepcopy(ctickets)))
    return '{} {}'.format(rides, promotions)


if __name__ == '__main__':
    lines = sys.stdin.readlines()
    T = int(lines[0])
    i = 1
    for t in range(1,T+1):
        N, C, M = (int(x) for x in lines[i].split())
        tickets = []
        for j in range(i+1, i+1+M):
            tickets.append(tuple(int(x) for x in lines[j].split()))
        i += 1+M
        print('Case #{}: {}'.format(t, solve(N, C, tickets)))
