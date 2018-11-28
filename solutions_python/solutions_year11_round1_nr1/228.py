import sys, time, math

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


if __name__ == '__main__':
    main()
