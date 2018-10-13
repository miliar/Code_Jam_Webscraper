def flip(pac, start, S):
    for i in xrange(S):
        pac[start + i] = not pac[start + i]

    return pac

def solve(pac, S):
    kLen = len(pac)

    for cnt in xrange(kLen):
        if pac.count(False) == 0:
            return cnt

        bIdx = pac.index(False)
        #print bIdx, S, kLen
        if S + bIdx > kLen:
            return "IMPOSSIBLE"

        pac = flip(pac, bIdx, S)
        #print pac
    return "IMPOSSIBLE"

def parseK(Kin):
    pac = [False] * len(Kin)

    for i in xrange(len(Kin)):
        if Kin[i] == "+":
            pac[i] = True

    return pac

T=int(raw_input())
for cas in xrange(1,T+1):
    K, strS=map(str, raw_input().split())
    S = int(strS)
    #graph = [int(n) - 1 for n in raw_input().split()]
    #[J, P, S, K] = [int(x) for x in raw_input().split()]
    #print K, S
    pacList = parseK(K)
    #print pacList, pacList.count(1), pacList.count(0)
    print "Case #{}: {}".format(cas,solve(pacList, S))


#("1{0:0>"+str(sub-2)+"b}1").format(i)
#("1{0:07b}1").format(10)

#print "Case #1:"
#for i in res:
#    print i," ".join(divs)





