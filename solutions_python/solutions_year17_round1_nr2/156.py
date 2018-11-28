#!/usr/bin/python3

LO = 0.8999999
HI = 1.1000001

def solve():
    N,P = (int(i) for i in input().strip().split())
    rat = [int(i) for i in input().strip().split()]
    amounts = [sorted([int(i)/rat[n] for i in input().strip().split()]) for n in range(N)]

    kits = 0
    servs = 1
    while servs < 1000001:
        if min([amounts[n][0]/servs for n in range(N)]) > 2.5:
            servs = servs * 2
            continue
        if min([amounts[n][0]/servs for n in range(N)]) > 1.2:
            servs = (servs * 10) // 9 + 1
            continue
        for n in range(N):
            while(amounts[n][0]/servs < LO):
                amounts[n].pop(0)
                if len(amounts[n]) == 0:
                    return kits
        while(all(LO <= amounts[n][0]/servs <= HI for n in range(N))):
            kits += 1
            for i in range(N):
                amounts[i].pop(0)
                if len(amounts[i]) == 0:
                    return kits
        servs += 1

    return kits

T = int(input())
for t in range(1, T+1):
    ans = solve()
    print("Case #%d: %d" % (t, ans))
