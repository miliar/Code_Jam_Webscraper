import math
#f = open('A.in', 'r')
f = open('A-large.in', 'r')
g = open('outputfile.out', 'w')

T= int(f.readline())
myoutput = []



for i in range(1,T+1):
    surface = 0
    maxsurface = 0
    pancakesheights = []
    pancakesradiuses = []

    [N, K] = f.readline().strip().split(' ')
    [N, K] = [int(N),int(K)]
    print(i)
    for nn in range(N):
        [R, H] = f.readline().strip().split(' ')
        [R, H] = [int(R), int(H)]
        obsahbokov = 2*math.pi*R*H
        pancakesheights.append((nn,obsahbokov, R))#ID, obsahbokov, R
        pancakesradiuses.append((nn, obsahbokov, R))

    pancakesheights = sorted(pancakesheights, key=lambda x: x[1])
    pancakesradiuses = sorted(pancakesradiuses, key=lambda x: x[2])

    for rr in range(N-1,K-1-1,-1):
        surface = pancakesradiuses[rr][1]#obsah bokov
        polomer = pancakesradiuses[rr][2]
        surface += math.pi*polomer*polomer
        pancakeID = pancakesradiuses[rr][0]
        pocet=0
        hh = N-1
        while pocet<(K-1):
            pancakeID2 = pancakesheights[hh][0]
            if(pancakeID !=pancakeID2):
                surface +=pancakesheights[hh][1]#obsah bokov
                pocet+=1
            hh-=1
        if surface>maxsurface:
            maxsurface = surface
    myoutput.append(maxsurface)

for i in range(1,T+1):
    g.write("Case #{}: {} \n".format(i, myoutput[i-1]))

f.close()
g.close()