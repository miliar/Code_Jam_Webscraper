#!/usr/bin/python2
""" INPUT """
def solve(C, D, P, V):
    def fix(blocks):
        if len(blocks) == 1: return
        (s2,t2,d2) = blocks[len(blocks)-1]
        (s1,t1,d1) = blocks[len(blocks)-2]
        if t1 <= s2: return # no intersection; no worries
        blocks.pop()
        blocks.pop()
        overlap = t1 - s2
        if d2 + overlap <= d1:
            blocks.append((s1,t2+overlap,d1))
        elif d1 + overlap <= d2:
            blocks.append((s1-overlap,t2,d2))
        else:
            dnew = .5* (d1 + d2 + overlap)
            blocks.append((s1-(dnew - d1),
                           t2+(dnew - d2),
                           dnew))
        fix(blocks)

    blocks = []
    for i in range(C):
        blocks.append((P[i] - .5*V[i],
                       P[i] + .5*V[i],
                       .5*(V[i]-1)))
        fix(blocks)
    
    return max([b[2] for b in blocks])

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
        C, D = (int (x) for x in lines.pop().split(' '))
        P,V = range(0,C), range(0,C)
        for i in range(0,C):
            (P[i], V[i]) = (int (x) for x in lines.pop().split(' '))
        SP = [1.0*P[i]/D for i in range(C)]
        result =D * solve (C,D,SP,V)
        fout.write('Case #%s: %s\n' % (CASE, result))

main()
