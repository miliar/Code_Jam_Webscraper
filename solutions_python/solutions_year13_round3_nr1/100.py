import sys

#sys.stdin = open('temp.txt', 'r')
sys.stdin = open('A-large.in')
sys.stdout = open('op.out', 'w')


def solve(tc):

    [s, n] = raw_input().split(' ')
    n = int(n)

    f = [0]*len(s)
    g = [0]*len(s)
    #print s, ' ', n

    if s[0] in ['a', 'e', 'i', 'o', 'u']:
        f[0] = 0
        g[0] = 0
    else:
        g[0] = 1
        if n==1:
            f[0] = 1
        else:
            f[0] = 0

    #print s[0], ' ', g[0], ' ', f[0]

    for i in range(1, len(s)):
        if s[i] in ['a', 'e', 'i', 'o', 'u']:
            g[i] = 0
            f[i] = f[i-1]
        else:
            g[i] = g[i-1] + 1
            if g[i-1] >= (n-1):
                f[i] = i - n + 2
            else:
                f[i] = f[i-1]

        #print s[i], ' ', g[i], ' ', f[i]

    print 'Case #' + str(tc) + ': ' + str(sum(f))
    #print g, f
    #print '\n\n'


def main():
    t = int(raw_input())
    for tc in range(1, t+1):
        solve(tc)

main()
