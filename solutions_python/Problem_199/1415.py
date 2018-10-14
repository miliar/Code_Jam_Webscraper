import sys
sys.setrecursionlimit(100000)


def getPath(v,k,f):
    if not False in [v[i] == 1 for i in range(len(v))]:
        return str(f)
    for i in range(len(v)):
        if v[i] == 0:
            if len(v)-i < k:
                return 'IMPOSSIBLE'
            else:
                return getPath(swap(v,i,k),k,f+1)

def swap(v,i,k):
    for j in range(i,i+k):
        v[j] = 1^v[j]
    return v

p1 = open('file','r')
p = p1.read().split('\n')[1:]
i = 1
o = open('out.txt','w')
for l in p:
    k = int(l.split()[1])
    l = l.split()[0]
    s = map(lambda x: 0 if x=='-' else 1 ,list(l))
    t = getPath(s,k,0)
    #print t
    o.write('Case #' + str(i) + ': ' + t + '\n')
    i += 1
    
    
p1.close()
o.flush()
o.close()

    
    