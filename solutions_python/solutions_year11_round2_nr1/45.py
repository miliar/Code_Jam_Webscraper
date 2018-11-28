#!/usr/bin/python2
""" INPUT """
def solve(N, M):
    pass

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
        N = int (lines.pop())
        S = [lines.pop() for i in range(N)]
        P = [[int(s[i]!='.') for i in range(N)] for s in S]
        W = [[int(s[i]=='1') for i in range(N)] for s in S]
        NW = [sum([int(i) for i in W[me]]) for me in range(N)]
        NP = [sum([int(i) for i in P[me]]) for me in range(N)]
        WP = [1.0 * NW[me] / NP[me] for me in range(N)]

        OWP = range(N)
        OOWP = range(N)
        for me in range(N):
            total = 0
            for opp in range(N):
                if P[me][opp]: # We played each other
                    total += 1.0 * (NW[opp] - W[opp][me]) / (NP[opp]-1)
            OWP[me] = total / NP[me]
        for me in range(N):
            total = 0
            for opp in range(N):
                if P[me][opp]: # We played each other
                    total += OWP[opp]
            OOWP[me] = total / NP[me]
        RPI = [.25 * WP[i] + .5 * OWP[i] + .25 * OOWP[i] for i in range(N)]
        result = "\n".join([str(n) for n in RPI])
        fout.write('Case #%s:\n%s\n' % (CASE, result))

main()
