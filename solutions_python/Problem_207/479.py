import sys

def solve(N,R,O,Y,G,B,V):
    P = [(R,'R'),(Y,'Y'),(B,'B')]
    P.sort()
    #print (P)

    result=['x']*N
    for i in range(3):
        if (P[i][0]>N/2):
            return "IMPOSSIBLE"

    for i in range(P[2][0]):
        result[i*2]=P[2][1]

    m = N//2+N%2
    if (P[2][0] < m):
        for i in range(P[2][0], m):
            result[i*2]=P[1][1]
        (x,y) = P[1]
        x -= (m-P[2][0])
        P[1] = (x,y)

    for i in range(P[1][0]):
        result[i*2+1]=P[1][1]

    s = ''.join(result)
    s = s.replace('x',P[0][1])

    return s


if __name__=='__main__':

    T = int(sys.stdin.readline())
    for i in range(T):
        (N,R,O,Y,G,B,V) = (int(x) for x in sys.stdin.readline().rstrip().split())
        y = solve(N,R,O,Y,G,B,V)

        print("Case #%d: %s" % (i+1, y))
