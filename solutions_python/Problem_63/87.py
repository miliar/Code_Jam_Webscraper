# Problem B of Google Code Jam 2010 Round-1 Sub-3

def worst_case(l):
    if l==1 or l==0:
        return l
    return 1+worst_case((l-1)-(l-1)/2)


def load_testing(l,p,c):
    a=[]
    t=l*c
    while t<p:
        t *= c
        a.append(t)
    la = len(a)
    # print a
    return worst_case(la)

if __name__ == '__main__':
    n = int(raw_input())
    for i in range(1,n+1):
        line = raw_input()
        line = line.split()
        print 'Case #%d: %d'%(i,load_testing(int(line[0]),int(line[1]),int(line[2])))
