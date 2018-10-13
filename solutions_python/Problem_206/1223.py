# TODO: strip split


#f = open('A.in', 'r')
f = open('A-large.in', 'r')
g = open('outputfile.out', 'w')

T= int(f.readline())
myoutput = []
maxtime = 0
for i in range(1,T+1):
    maxtime = 0
    D,N = f.readline().strip().split(' ')
    N = int(N)
    D = int(D)
    for j in range(1, N + 1):
        K, S = f.readline().strip().split(' ')
        K = int(K)
        S = int(S)
        time = (D-K)/S
        if time>maxtime:
            maxtime=time

    myoutput.append(D/maxtime)


for i in range(1,T+1):
    g.write("Case #{}: {} \n".format(i, myoutput[i-1]))

f.close()
g.close()