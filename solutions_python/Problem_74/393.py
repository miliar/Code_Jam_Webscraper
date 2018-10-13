import sys, time, math
#import psyco

def main():  # gcj 2011 round 0 A
    sys.stdin = open("in.txt","r")
    sys.stdout = open("out.txt","w")
    T = int(input())
    for case in range(T):
        NL = (input()).split()
        N = int(NL[0])
        ow, bw, total = 1, 1, 0
        for i in range(1,2*N+1,2):
            on, bn = -1, -1
            for j in range(i,2*N+1,2):
                if NL[j]=='O':
                    on = int(NL[j+1])
                    break
            for j in range(i,2*N+1,2):
                if NL[j]=='B':
                    bn = int(NL[j+1])
                    break
            #print(ow,bw,on,bn,total)
            if on==-1:
                if bn==-1: print("wrong!")
                else:
                    total = total+abs(bn-bw)+1
                    bw = bn
            else:
                if bn==-1:
                    total = total+abs(on-ow)+1
                    ow = on
                else:
                    if NL[i]=='O':
                        total = total+abs(on-ow)+1
                        if abs(bn-bw)<=abs(on-ow)+1:
                            bw = bn
                        else:
                            if bw<bn: bw = bw+abs(on-ow)+1
                            else: bw = bw-abs(on-ow)-1
                        ow = on
                    else:
                        total = total+abs(bn-bw)+1
                        if abs(on-ow)<=abs(bn-bw)+1:
                            ow = on
                        else:
                            if ow<on: ow = ow+abs(bn-bw)+1
                            else: ow = ow-abs(bn-bw)-1
                        bw = bn
                    
        print("Case #",case+1,": ",total,sep='')
    return 0

"""
class List():
    def __init__(self, n, m):
        self.edge = [None] * m
        self.init( n )
        
    def init(self, n):
        self.end = n
        for i in range(n):
            self.edge[i] = [ i, -1, 0 ]
            
    def append(self, u, v, w):
        end = self.end
        item, link, cost = self.edge[u]
        self.edge[end] = [ v, link, w ]
        self.edge[u] = [ item, end, cost ]
        self.end += 1

    def show(self, n):
        for i in range(n):
            j = i
            while self.edge[j][1]!=-1:
                j = self.edge[j][1]
                print(self.edge[j][0],end=' ')
            print('')

def SPFA(n, m, List, start):
    d = [ -1 for x in range(n) ]
    d[start] = 0
    queue = [ 0 for x in range(10*n) ]
    head, tail, queue[0] = 0, 1, start
    while head!=tail:
        u = queue[head]
        head += 1
        j = u
        while List.edge[j][1]!=-1:
            j = List.edge[j][1]
            v, w = List.edge[j][0], List.edge[j][2]
            if d[v]==-1 or d[v]>d[u]+w:
                d[v] = d[u]+w
                queue[tail] = v
                tail += 1
    return d

def SPFA(n, bn, b, start):
    d = [ -1 for x in range(n) ]
    d[start] = 0
    queue = [ 0 for x in range(10*n) ]
    head, tail, queue[0] = 0, 1, start
    while head!=tail:
        u = queue[head]
        head += 1
        for i in range(bn):
            v, w = u+b[i], 1
            if v>=n: w, v = 0, v-n
            if d[v]==-1 or d[v]>d[u]+w:
                d[v] = d[u]+w
                queue[tail] = v
                tail += 1
    
    return d

def main():  # gcj 2010 round 3 B
    sys.stdin = open("in.txt","r")
    sys.stdout = open("out.txt","w")
    T = int(input())
    #List1 = List( 100000, 20000000 )
    for case in range(T):
        LN = (input()).split()
        L, N = int(LN[0]), int(LN[1])
        B = (input()).split()
        b = [ int(B[x]) for x in range(N) ]

        n = max(b)
        d = SPFA( n, N, b, 0 )
        print("Case #",case+1,":",sep='',end=' ')
        if d[L%n]==-1:
            print("IMPOSSIBLE")
        else:
            print(d[L%n]+L//n)

    return 0
"""


"""
def Prim( prim, n, vis ):
    pn = 0
    for i in range(2,n):
        if vis[i]==0: prim[pn], pn = i, pn+1
        for j in range(0,pn):
            if prim[j]*i>=n: break
            vis[prim[j]*i] = 1
            if i%prim[j]==0: break
    return pn

def PowMod( x, n, Mod ):
    s, t = 1, x
    while n!=0:
        if n%2 != 0: s = (s*t)%Mod
        n //= 2
        t = (t*t)%Mod
    return s%Mod

def Inv( x, Mod ):
    return PowMod( x, Mod-2, Mod );

def main():  # gcj 2010 round 3 A
    #print( Inv(4,1217) )
    sys.stdin = open("in.txt","r")
    sys.stdout = open("out.txt","w")
    
    N = 1000000
    prim = [ 0 for x in range(0,N) ]
    ok = [ 0 for x in range(0,N) ]
    pn = Prim( prim, N, ok )
    #print(pn,"ok")

    T = int(input())
    case = 0
    while T>0:
        T -= 1
        
        DK = (input()).split()
        D, K = int(DK[0]), int(DK[1])
        num = (input()).split()
        
        case += 1
        print("Case #",case,":",sep='',end=' ')
        
        if K==1: print("I don't know.")
        else:
            if K==2:
                if num[0]==num[1]: print(int(num[0]))
                else: print("I don't know.")
            else:
                mx = int( max( num ) )
                x, y, z, result = int(num[0]), int(num[1]), int(num[2]), -1
                for i in range(0,pn):
                    if prim[i]<=mx: continue
                    if prim[i]>pow(10,D): break

                    zy, yx = z-y, y-x
                    if yx<0: zy, yx = -zy, -yx

                    A = (zy * Inv( yx, prim[i] ))%prim[i]
                    B = (y-A*x)%prim[i]

                    w = z
                    for j in range(3,K):
                        w = (A*w+B)%prim[i]
                        if int(num[j])!=w: break
                    else:
                        value = (A*int(num[K-1])+B) %prim[i]
                        #print(A,B,result,value)
                        if result==-1: result = value
                        else:
                            if result!=value:
                                result = -1
                                break
                print( result==-1 and "I don't know." or result )
        
    return 0
"""


"""
def main():  # spoj 0002  TLE
    #st = time.clock()
    prim = [ 0 for x in range(0,1000000) ]
    ok = [ 0 for x in range(0,1000008) ]
    pn = Prim( prim, 1000000, ok )
    print(pn,prim[:pn])

    #end = time.clock()
    #print( end-st )

    t = int(input())
    for tt in range(0,t):
        mn = input()
        mn = mn.split()
        m = int(mn[0])
        n = int(mn[1])

        if m==1:
            m += 1
        
        #for i in range(0,n-m+1):
        #    ok[i] = 0
        #for i in range(0,n-m+1):
        #    print(ok[i],end=' ')
        #print()
        ok[0:n-m+1:1] = [0 for x in range(0,n-m+1)]
        #for i in range(0,n-m+1):
        #    print(ok[i],end=' ')
        #print()
        #ok = [ 0 for x in range(0,n-m+1) ]

        sn = math.sqrt(n)+1
        for i in range(0,pn):
            if prim[i]>sn:
                break
            for j in range(m//prim[i],n//prim[i]+1):
                if( j*prim[i]>=m and j!=1 ):
                    ok[j*prim[i]-m] = 1

        #g = lambda x : x
        #print( [ x for x in range(m,n+1) if ok[x-m]==0 ] )
        #print( info )
        
        for i in range(0,n-m+1):
            if ok[i]==0:
                print(m+i)
    return 0
"""


"""
n = int(input())  # spoj 00001
while n!=42:
    print(n)
    n = int(input())
"""

if __name__ == '__main__':
    main()
