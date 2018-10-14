# solve legitly if time remaining

fin = open("C.in")
fout = open("C.out","w")

t = int(fin.readline())

def getlimits(L,i):
    l = i-1
    while not L[l]:
        l -= 1
    r = i+1
    while not L[r]:
        r += 1
    return (min(i-1-l,r-(i+1)), max(i-1-l,r-(i+1)))

for trial in range(1,t+1):
    N, K = [int(i) for i in fin.readline().strip().split()]
    L = [True]+[False]*N+[True]
    res = ''
    for ki in range(K):
        limits = [(j,getlimits(L,j)) for j in range(1,N+1) if not L[j]]
        #print(limits)
        maxmin = max(i[1][0] for i in limits)
        potential = [i for i in limits if i[1][0] == maxmin]
        if len(potential) > 1:
            maxmax = max(i[1][1] for i in potential)
            potential = [i for i in potential if i[1][1] == maxmax]
        L[potential[0][0]] = True
        if ki == K-1:
            maxmin, maxmax = getlimits(L,potential[0][0])
            res = str(maxmax)+' '+str(maxmin)
        #print(''.join('01'[int(i)] for i in L))
    # --------------------------------------------------------------------------
    print("Case #"+str(trial)+": "+res)
    fout.write("Case #"+str(trial)+": "+res+'\n')
