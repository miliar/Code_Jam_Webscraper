import sys
import fileinput

def eval(T, loc, m):
    if 2*loc > m:
        return T[loc]

    l = eval(T, 2*loc, m)
    r = eval(T, 2*loc+1, m)

    if T[loc]:
        return (l and r)
    return (l or r)

def solve(T, E, V, index):
    if eval(T, 1, len(T)-1) == V:
        return 0

    if index > len(T): 
        return -1

    min = 100000000
    for i in range(index, len(T)):
        if E[i]:
            T[i] = not T[i]
            ret = solve(T, E, V, i+1)
            if ret >= 0:
                if 1 + ret < min:
                    min = 1 + ret
            T[i] = not T[i]

    if min == 100000000:
        return -1
    else:
        return min


if __name__ == '__main__':
    lines = fileinput.input(sys.argv[1])
    num = int(lines.readline())
    for i in range(1, num+1):
        T = [0]
        E = [0]
        (M, V) = map(long, lines.readline().split(' '))
        for j in range(0, (M-1)/2):
            (G, C) = map(lambda x: int(x) == 1, lines.readline().split(' '))
            T.append(G)
            E.append(C)

        for j in range(0, (M+1)/2):
            v = int(lines.readline()) == 1
            T.append(v)
            E.append(False)

        out = solve(T, E, bool(V), 0)
        if out == -1:
            out = "IMPOSSIBLE"

        print 'Case #%d: %s' % (i, out)


