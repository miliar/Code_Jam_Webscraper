from itertools import takewhile


f = open("D.in", "r")

T = int(f.readline())

for i in range(T):
    N = int(f.readline())
    naomis = sorted([float(a) for a in f.readline().split()])
    kens = sorted([float(a) for a in f.readline().split()])
    
    fair = N
    k, n = 0, 0
    while k < len(kens) and n < len(naomis):
        if kens[k] > naomis[n]:
            k, n = k + 1, n + 1
            fair -= 1
        else:
            k += 1

    unfair = 0
    n, k = 0, 0
    for nvm in range(len(kens)):
        if kens[k] > naomis[n]:
            n += 1
        else:
            k += 1
            n += 1
            unfair += 1

#    naomis = list(reversed(naomis))
#    kens = list(reversed(kens))
#    unfair = 0
#    n, k = 0, 0
#    for nvm in range(len(kens)):
#        if kens[k] > naomis[n]:
#            k += 1
#        else:
#            n += 1
#            unfair += 1


#    naomis = reversed(naomis)
#    unfair = len(list(takewhile(lambda t: t[0] > t[1], zip(naomis, kens))))    

    print "Case #" + str(i + 1) + ": " + str(unfair) + " " + str(fair)
