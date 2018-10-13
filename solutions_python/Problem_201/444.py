def divide((n,p)):
    if n%2 == 0: return [(n/2,p) , ((n/2)-1,p)]
    else: return [(n/2,p), (n/2, p)]

def reduceCount(listofN):
    from collections import defaultdict
    d = defaultdict(list)
    for k,v in listofN:
        d[k].append(v)
    e = defaultdict(list)
    for k, v in d.items():
        e[k]=sum(v)
    temp = e.items()
    temp.sort(reverse=True)
    return temp
    

def findMinMax(N,k):
    emptyStalls = [(N,1)]
    min_max = [0,0]
    while k > 0:
        emptyStalls = reduceCount(emptyStalls)
        #print emptyStalls 
        a = emptyStalls[0]
        emptyStalls = emptyStalls[1:]
        countOfMax = a[1]
        temp = divide(a)
        for t in temp:
            emptyStalls.append(t)
        k-=countOfMax
        
    return [temp[0][0], temp[1][0]]

    
import sys

inputFile = sys.argv[1]
outFile = sys.argv[2]

fo = open(outFile, 'w')

with open(inputFile, 'r') as f:
    t = int(f.readline())
    for i in range(t):
        n, K = map(int, f.readline().strip().split(' '))
        lsLR = findMinMax(n,K)
        out =  "Case #{}: {} {}".format(i+1, lsLR[0], lsLR[1])
        fo.write(str(out)+'\n')

fo.close()


