from sys import stdin

def time(distances,vitesses):
    N = len(distances)
    L = []
    for i in range(N):
        L.append(distances[i]/vitesses[i])
    return max(L)

def speed(D,distances,vitesses):
    t = time(distances,vitesses)
    return D/t






T=int(stdin.readline())
for case in range(1,T+1):
        c=stdin.readline()
        data=c.split()
        D = int(data[0])
        N = int(data[1])
        distances = []
        vitesses = []
        for i in range(N):
            cc = stdin.readline()
            dataa = cc.split()
            distances.append(D-int(dataa[0]))
            vitesses.append(int(dataa[1]))
            v = str(speed(D,distances,vitesses)    )
        print('Case #%i: %s' % (case,v))


