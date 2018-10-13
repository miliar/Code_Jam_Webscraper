f = open('4.txt', 'r')
T = int(f.readline())

for t in range(T):
    N = int(f.readline())
    n = sorted(map(float, f.readline().split(' ')))
    k = sorted(map(float, f.readline().split(' ')))

    n1 = [x for x in n]
    k1 = [x for x in k]
    w=0
    for i in range(N):
        if n1[0] < k1[-1]:
            del k1[[x>n1[0] for x in k1].index(True)]
            del n1[0]
        else:
            del n1[0]
            del k1[0]
            w+=1

    dw = 0
    for i in range(N):
        if n[0] < k[0]:
            del n[0]
            del k[-1]
        else:
            del n[0]
            del k[0]
            dw += 1

    print "Case #{}: {} {}".format(t+1, dw, w)

f.close()
