# TODO: strip split


f = open('C.in', 'r')
#f = open('B-large.in', 'r')
g = open('outputfile.out', 'w')

T= int(f.readline())

myoutput = []
miesta = []
globalindex = 0

def vloz(X):
    global globalindex
    global miesta
    j=globalindex
    while (j<len(miesta)) and (miesta[j][0]!=X):
        j+=1
    if (j<len(miesta)):
        miesta[j][1]+=1
    else:
        miesta.append([X,1])

def processInput(N,K):
    global globalindex
    global miesta
    L=N
    R=N
    miesta.append([N,1])
    for kk in range(K):
        [actualN,actualCount] = miesta[globalindex]
        #ak parne
        if actualN%2==0:
            L = actualN//2
            R = L-1
        #ak neparne
        else:
            L = actualN//2
            R = L

        vloz(L)
        vloz(R)

        actualCount-=1
        miesta[globalindex] = [actualN,actualCount]
        if actualCount<=0:
            globalindex += 1



    return [L,R]

for i in range(1,T+1):
    N,K = f.readline().strip().split(' ')
    N = int(N)
    K = int(K)
    miesta = []
    globalindex = 0

    myoutput.append(processInput(N,K))


for i in range(1,T+1):
    g.write("Case #{}: {} {}\n".format(i, myoutput[i-1][0], myoutput[i-1][1]))

f.close()
g.close()