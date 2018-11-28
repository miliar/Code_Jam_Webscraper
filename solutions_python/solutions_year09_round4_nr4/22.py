import psyco
psyco.full()

def getbase(n, base, digit=None):
    ret=[]
    while (True):
        if (n<base):
            ret.append(n)
            break
        r=n%base
        n=n/base
        ret.append(r)
    ret.reverse()
    if digit!=None:
        ret=[[]]*(digit-len(ret))+ret
    return ret

def dis(x,y):
    d=((((0.+x[1]-y[1])**2 + (0.+x[0]-y[0])**2 ) ** 0.5)+ x[2]+y[2]) / 2.0
    return d
    
def solve(data):
    r=1000000
    if len(data)==3:
        r=min(r, max(dis(data[0],data[1]), data[2][2]))
        r=min(r, max(dis(data[1],data[2]), data[0][2]))
        r=min(r, max(dis(data[0],data[2]), data[1][2]))
        return r
    elif len(data)==2:
        return max(data[0][2], data[1][2])
    else:
        return data[0][2]
        
caseNum=input()
for caseId in xrange(1, caseNum+1):
    plantNum=input()
    data=[]
    for i in xrange(plantNum):
        data.append([int(e) for e in raw_input().split()])
    print "Case #%d: %.6f" % (caseId, solve(data))