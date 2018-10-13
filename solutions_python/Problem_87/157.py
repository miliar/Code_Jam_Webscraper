#!/usr/bin/python2
def solve(X,S,R,t,N,B,E,w):
    Wd = sum([E[i] - B[i] for i in range(N)])
    W = [(0.0, X - Wd)] + [(0.0+w[i], 0.0+E[i] - B[i]) for i in range(N)] # Length of walkway
    W.sort()
    def solve(S, R, t, W):
        s = "W = %s" % W
        if not W:
            result = 0
        elif t == 0:
            speed = S+W[0][0]
            result = W[0][1] / speed + solve(S,R,t,W[1:])
        else:
            speed = R+W[0][0]
            time = W[0][1] / speed
            print "(%s, %s)" % (time, t)
            if time <= t:
                print "NOT EXPTR"
                result = W[0][1] / speed + solve(S,R,t-time,W[1:])
            else:
                print "EXTRAPOLATING"
                result = t + solve(S,R,0, [(W[0][0], W[0][1] * (1-t / time) )]  + W[1:])
        print "%s => %s" % (s, result)
        return result
    return solve(S,R,t,W)

def main():
    import sys
    input = sys.argv[1]
    output = input.replace('in', 'out')
    fin = open(input, 'r')
    fout = open(output, 'w')
    lines = [line.strip() for line in fin]
    lines.reverse()

    T = int(lines.pop())
    for CASE in range(1,T+1):
        (X,S,R,t,N) = (int (x) for x in lines.pop().split(' '))
        B,E,w = range(N), range(N), range(N)
        for i in range(N):
            B[i],E[i],w[i] = (int (x) for x in lines.pop().split(' '))
        result = solve(X,S,R,t,N,B,E,w)
        fout.write('Case #%s: %s\n' % (CASE, result))

main()
