



def isUntidy(N):
    t = map(int,[x for x in str(N)])
    sorted_t = sorted(t)
    if t==sorted_t:
        return False
    
    return True


def findLastTidy(n):
    if n%10==n: return n
    s = ''
    if isUntidy(n):
        s+=str(9)
        return str(findLastTidy((n/10)-1))+s
    else: return str(n)


import sys

inputFile = sys.argv[1]
outFile = sys.argv[2]

fo = open(outFile, 'w')

with open(inputFile, 'r') as f:
    #print f.readline()
    t = int(f.readline())
    for i in range(t):
        r = int(f.readline().strip())
        out =  "Case #{}: {}".format(i+1, str(int(findLastTidy(r))))
        fo.write(str(out)+'\n')

fo.close()


        
