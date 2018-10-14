#!/usr/bin/env python2.5

import psyco
psyco.full()

G_OR, G_AND = 0, 1

def evaluate(gates, values):
    for i in reversed(range(1, len(gates))):
        if gates[i] == G_AND:
            values[i] = values[2*i] & values[2*i+1]
        else:
            values[i] = values[2*i] | values[2*i+1]
    return values[1]

def solve_case(V, gates, changables, values):
    changable_indexes = [i for i in range(1, len(gates)) if changables[i] == 1]
##    print changable_indexes
    best = 'IMPOSSIBLE'
    for i in range(2 ** len(changable_indexes)):
        changes = 0
        changed_gates = list(gates)
        for (b, c) in enumerate(changable_indexes):
            if (i >> b) & 1:
                changed_gates[c] ^= 1
                changes += 1
        if evaluate(changed_gates, values) == V:
            if best == 'IMPOSSIBLE' or changes < best:
                best = changes
##            print changes, 'good'
##        else:
##            print changes
    return best

def main(lines):
    lines = (line.strip() for line in lines)
    
    N = int(lines.next())
    for case in range(1, N + 1):
        M, V = [int(d) for d in lines.next().split()]
        # interior nodes
        gates = [-1]
        changables = [-1]
        for i in range((M - 1)//2):
            G, C = [int(d) for d in lines.next().split()]
            gates.append(G)
            changables.append(C)
        values = [-1] * (1 + (M - 1)//2)
        for i in range((M + 1)//2):
            values.append(int(lines.next()))

        print "Case #%s: %s" % (case, solve_case(V, gates, changables, values))
        
if __name__ == '__main__':
    import fileinput
    main(fileinput.input())
