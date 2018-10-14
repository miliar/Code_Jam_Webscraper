def dGame(N, K):
    N.sort()
    N.reverse()
    K.sort()
    K.reverse()
    Nwin = 0
    latch = 0
    for i in range(0,len(N)):
        for j in range(latch,len(K)):
            if(N[i]>K[j]):
                Nwin = Nwin+1
                latch = j+1
                break;
    return Nwin        
                
def game(N, K):
    return len(N) - dGame(K,N)

##L1 = [0.5, 0.1, 0.9]
##L2 = [0.6, 0.4, 0.3]
##
##print str(dGame(L1, L2)) + " " + str(game(L1, L2))

T = int(raw_input())
B = open('GCJ2k14A3.out','w')
for i in range(1, T+1):
    n = int(raw_input())
    N = raw_input().split(' ')
    for j in range(0, len(N)):
        N[j] = float(N[j])
    K = raw_input().split(' ')
    for j in range(0, len(K)):
        K[j] = float(K[j])
    B.write("Case #" + str(i) + ": " + str(dGame(N,K)) + " " + str(game(N,K)) + "\n")
B.close()
