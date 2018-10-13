T = int(input())
for t in range(T):
    N = input()
    Nlist = [int(c) for c in N]
    l = len(Nlist)
    i = 0
    j = 0
    while i < l - 1 and Nlist[i] <= Nlist[i + 1]:
        if Nlist[i] < Nlist[i + 1]:
            j = i + 1
        i += 1
    if i < l - 1:
        Nlist[j] -= 1
        for k in range(j + 1, l):
            Nlist[k] = 9
        N = ''.join([str(n) for n in Nlist])
        if N[0] == '0':
            N = N[1:]
    print("Case #" + str(t + 1) + ": " + N)
