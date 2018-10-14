"""Problem A"""

def main():
    t = input()
    for i in range(1,t+1):
        K = []
        S = []
        minTime = [] # min time at which each horse can reach dest
        D,N = [int(s) for s in raw_input().split(" ")]
        for j in range(N):
            Kj,Sj = [int(s) for s in raw_input().split(" ")]
            K.append(Kj)
            S.append(Sj)
            minTimej = (D-Kj)/float(Sj) # t = distance/maxspeed
            minTime.append(minTimej)

        #index = minTime.index(min(minTime))
        speed = D/float(max(minTime))
        print("Case #{}: {}".format(i,speed))

main()
