#!/usr/bin/env python3

cases = int(input())

for T in range(1, cases+1):
    N = int(input())
    workers = [[n for n, c in enumerate(input()) if c == '1'] for _ in range(N)]

    fu = [i for i in range(N)]
    qty = [0 for i in range(N)]
    def find(x):
        if fu[x] != x:
            fu[x] = find(fu[x])
        return fu[x]
    def union(x, y):
        fu[find(x)] = find(y)
    def group(x):
        return [i for i in range(N) if find(i)==x]

    groups = []
    for worker in workers:
        if len(worker) > 0:
            fst = worker[0]
            for mach in worker[1:]:
                union(fst, mach)

    result = 0

    for worker in workers:
        if len(worker) > 0:
            qty[find(worker[0])] += 1
    
    cont = True
    while cont:
        cont = False
        for i in range(N):
            if qty[i] > len(group(i)):
                cont = True
                grs = sorted([(len(group(x)), x) for x in range(N) if len(group(x)) > qty[x]])
                _, nr = grs[0]
                qty[i] += qty[nr]
                qty[nr] = 0
                union(nr, i)
        


    for worker in workers:
        if len(worker) > 0:
#            qty[find(worker[0])] += 1
            for x in group(find(worker[0])):
                if x not in worker:
                    result += 1

    for worker in workers:
        if len(worker) == 0:
            grs = sorted([(len(group(x)), x) for x in range(N) if len(group(x)) > qty[x]])
            # print(grs)
            _, nr = grs[0]
            qty[nr] += 1
            result += len(group(nr))

                
            

    #for i in range(N):
    #    print("{} -> {} / {} / {}".format(i, find(i), group(i), qty[i]))
    #print(workers)
    print("Case #{}: {}".format(T, result))

    
