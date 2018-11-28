

def findminstalls(stalls, people):
    #print(stalls, people)
    #ouf.write("\t{} {}\n".format(stalls,people))
    if stalls == people:
        return (0, 0)
    R = stalls // 2
    L = R + stalls % 2 - 1
    minS = min(L, R)
    maxS = max(L, R)
    if people == 1:
        return (maxS, minS)
    if people % 2 == 0:
        return (findminstalls(maxS, people // 2))
    return (findminstalls(minS, people // 2))


ouf = open('output.txt', 'w')

with open('C-large.in', 'r') as inf:
    t = int(inf.readline())
    for i in range(1, t+1):
        N, K = (int(x) for x in inf.readline().split())
        #ouf.write(" {} {}\n".format(N, K))
        a = findminstalls(N, K)
        ouf.write("Case #{}: {} {}\n".format(i, a[0], a[1]))


ouf.close()
        
        
