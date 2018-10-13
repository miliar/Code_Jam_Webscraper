f = open('C small input.in','r')
a = f.read()
f.close()
b = a.split('\n')
del(b[-1])


#This works because this is for small input only!
def recycle(n,m):#n != m
    N,M = str(n),str(m)
    if len(N) != len(M):
        return False
    elif len(N) == 1 or len(M) == 1:
        return False
    elif len(N) == 4 or len(M) == 4:
        return False
    else:
        if len(M) == 3:
            l1 = [M[1],M[2],M[0]]
            l2 = [M[2],M[0],M[1]]

            Nlist = [N[0],N[1],N[2]]
            if Nlist == l1 or Nlist == l2:
                return True
        elif len(M) == 2:
            l1 = [M[1],M[0]]
            Nlist = [N[0],N[1]]
            if Nlist == l1:
                return True
        return False
        
def solve(A,B):
    s = 0
    for n in range(A,B+1):
        for m in range(n+1,B+1):
            if recycle(n,m) == True:
                s = s + 1
    return s

g = open('C OutSmall.txt','w')
N = int(b[0])
for i in range(1,N+1):
    y = list(map(int,b[i].split(' ')))
    A,B = y[0],y[1]
    x = solve(A,B)
    #print(x)
    s = "Case #"+str(i) + ': '+str(x) + '\n'
    g.write(s)

g.close()
