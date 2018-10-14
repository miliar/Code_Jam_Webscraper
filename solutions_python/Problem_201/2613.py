i = 0
for each in range(int(input())):
    i += 1
    stall, n = map(int, input().split())
    Map = [stall]
    for p in range(n):
        Max = 0
        for each in range(len(Map)):
            Max = each if Map[each] > Map[Max] else Max
        l = Map[Max]//2 if Map[Max]%2 else Map[Max]//2 -1
        r = Map[Max]//2
        if l and r:
            Map[Max:Max+1] = [l, r]
        elif l:
            Map[Max:Max+1] = [l]
        elif r:
            Map[Max:Max+1] = [r]
        else:
            Map[Max:Max+1] = []
    print("Case #", i, ': ', r, ' ', l, sep='')