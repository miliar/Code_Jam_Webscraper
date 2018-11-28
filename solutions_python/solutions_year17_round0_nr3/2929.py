import time
def left(N, k):
    if N[k]: return -1
    n, k = 0, k-1
    while not N[k]:
        k -= 1
        n += 1
    return n
def right(N, k):
    if N[k]: return -1
    n, k = 0, k+1
    while not N[k]:
        k += 1
        n += 1
    return n
##s = time.time()
for _ in range(int(raw_input())):
    n, k = map(int, raw_input().split())
    N = [False] * (n+2)
    N[0] = True
    N[n+1] = True
    for __ in range(k):
        L_R = [(left(N, i), right(N, i)) for i in range(1, n+1)]
        Min = map(min, L_R)
        maximum = max(Min)
##        print L_R, Min, maximum
        considered = []
        for i in range(len(Min)):
            if Min[i] == maximum:
                considered.append((L_R[i], i))
##        print considered
        if len(considered) == 1:
            if __ == k-1:
                print "Case #{}: {} {}".format(_+1, max(considered[0][0]), min(considered[0][0]))
            N[considered[0][1]+1] = True
        else:
            Max = [max(c[0]) for c in considered]
            maximum = max(Max)
##            print Max, maximum
            index = considered[Max.index(maximum)][1]
##            print index, len(considered)
            N[index+1] = True
            if __ == k-1:
                print "Case #{}: {} {}".format(_+1, max(considered[Max.index(maximum)][0]), min(considered[Max.index(maximum)][0]))
##        print N
##print time.time() - s     
