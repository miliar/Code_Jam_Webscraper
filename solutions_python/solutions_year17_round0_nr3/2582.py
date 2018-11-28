import sys
sys.setrecursionlimit(10000000)
reload(sys)
def stall(distance, K):
    for i in range(len(distance)):
        if i >= len(distance):
            break
        if distance[i] == 0:
            distance.pop(i)
            i -= 1
    for i in range(len(distance)):
        if distance[i] == max(distance):
            d = distance.pop(i)
            break
    if d%2 == 0:
        d_min, d_max = d/2-1, d/2
    else:
        d_min, d_max = (d-1)/2, (d-1)/2
    if K == 1:
        return (d_max, d_min)
    else:
        distance += [d_min, d_max]
        return stall(distance, K-1)

inf = open(sys.argv[1])
inp = inf.read().split('\n')
inf.close()

T = int(inp.pop(0))
outf = open('output.txt','w')
for i in range(T):
    N, K = [int(x) for x in inp.pop(0).split(' ')]
    outf.write('Case #{0}: {1}\n'.format(i+1,' '.join([str(x) for x in stall([N],K)])))
outf.close()
