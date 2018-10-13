import sys, time, math

def main(): # gcj 2011 round 1
    sys.stdin = open("in.txt","r")
    sys.stdout = open("out.txt","w")
    T = int(input())
    for case in range(T):
        N = int(input())
        s = [ 0 for x in range(N) ]
        wp = [ 0 for x in range(N) ]
        owp = [ 0 for x in range(N) ]
        oowp = [ 0 for x in range(N) ]
        for i in range(N):
            s[i] = input()
        #print(s)
        print("Case #",case+1,": ",sep='',end='\n')
        for i in range(N):
            total, win = 0, 0
            for j in range(N):
                if s[i][j]!='.': total += 1
                if s[i][j]=='1': win += 1
            wp[i] = win/total

            owp[i], num = 0, 0
            for j in range(N):
                if s[i][j]=='.': continue
                num += 1
                total, win = 0, 0
                for k in range(N):
                    if i==k: continue
                    if s[j][k]!='.': total += 1
                    if s[j][k]=='1': win += 1
                owp[i] += win/total
            owp[i] = owp[i]/num
        #print(wp,owp)
        
        for i in range(N):
            oowp[i], num = 0, 0
            for j in range(N):
                if s[i][j]!='.':
                    num += 1
                    oowp[i] += owp[j]
            oowp[i] = oowp[i]/num
            print(0.25*wp[i]+0.5*owp[i]+0.25*oowp[i])

"""
def gcd( a, b ):
    if a>b: a, b = b, a
    if a==0: return b
    else: return gcd( b%a, a )

def lcm( a, b ):
    return a*b/gcd(a,b)

def main(): # gcj 2011 round 0 D
    sys.stdin = open("in.txt","r")
    sys.stdout = open("out.txt","w")
    T = int(input())
    for case in range(T):
        c = (input()).split()
        C = [ int(c[x]) for x in range(len(c)) ]
        N, Pd, Pg = C[0], C[1], C[2]
        
        print("Case #",case+1,": ",sep='',end='')
        x = lcm( Pd, 100 )
        #print( x, Pd, Pg, N );
        if Pd!=0 and x/Pd>N:
            print("Broken")
            continue
        low, up = 0, 100
        if Pd==0: low, up = 0, 99
        else:
            if Pd==100: low, up = 1, 100
            else: low, up = 1, 99
        
        #print( low, up );
        if Pg<low or up<Pg: print("Broken")
        else: print("Possible")

    return 0
"""

if __name__ == '__main__':
    main()
