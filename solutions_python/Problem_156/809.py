__author__ = 'lowikchanussot'

def time_wo_split(P) :
    return max(P)

def split(oldP) :
    P = sorted(oldP)
    to_split = P[-1]
    if P[-1] == 9 :
        P[-1] = 6
        P.append(3)
    elif to_split %2 == 0 :
        P[-1] = to_split/2
        P.append(to_split/2)
    else :
        P[-1] = to_split/2
        P.append(to_split/2 + 1)
    return P

def update(P) :
    return [x-1 for x in P]


def solve(P) :
    t = time_wo_split(P)
    if t <= 2 : return t
    return min(time_wo_split(P), solve(split(P))+1, solve(update(P))+1)


def solveBSmall(input, output) :
    with open(input, 'r') as inp, open(output, 'w') as out :
        lines = inp.readlines()
        T = int(lines[0])
        for i in range(T) :
            D = int(lines[2*i + 1])
            P = [int(w) for w in lines[2*i+2].split()]
            sol = solve(P)
            out.write("Case #%d: %d\n"%(i+1, sol))

if __name__ == '__main__':
    import sys
    import os
    _, input = sys.argv
    output = os.path.splitext(input)[0] + '.out'
    solveBSmall(input, output)
