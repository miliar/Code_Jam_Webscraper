
nT = int(input())

#dp1 = [[-1] * 10 for _ in range(1000)]
#
#def nbL(l, f = 1):
#    if l == 0: return 1
#    if dp1[l][f] == -1:
#        s = 0
#        for i in range(f, 10):
#            s += nbL(l-1, i)
#        dp1[l][f] = s
#    return dp1[l][f]

for iT in range(1, nT+1):
    print("Case #", iT, ": ", sep='', end='')

    n = int(input())
    tn = []
    nn = n
    while nn != 0:
        tn.append(nn % 10)
        nn //= 10
    tn = tn[::-1]
    for i in range(len(tn)):
        keep = False
        while tn[i] != 0 and not keep:
            keep = True
            for j in range(i+1, len(tn)):
                if tn[i] < tn[j]:
                    break
                if tn[i] > tn[j]:
                    keep = False
                    break
            if not keep:
                tn[i] -= 1
                for j in range(i+1, len(tn)):
                    tn[j] = 9

    i = 0
    while(tn[i] == 0):
        i += 1
    for j in range(i, len(tn)):
        print(tn[j], end='')
    print()
