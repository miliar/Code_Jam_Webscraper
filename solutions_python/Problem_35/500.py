#!/usr/bin/env python3

def j(M):
    ret = []
    table = {}
    c = 'a'
    for j in range(len(M)):
        r = []
        for i in range(len(M[0])):
            if table.get(M[j][i]) == None:
                table.update({M[j][i]: c})
                r.append(c)
                c = chr(ord(c)+1)
            else:
                r.append(table.get(M[j][i]))
        ret.append(r)
    return ret

def h(M, C, l):
    (x, y) = C
    (a, b) = l
    if 0 <= x < len(M[0]) and 0 <= y < len(M):
        if M[y][x] < M[b][a]:
            return C

    return l

def g(M, C):
    (x, y) = C

    l = h(M, (x, y-1), C)       # N
    l = h(M, (x-1, y), l)       # W
    l = h(M, (x+1, y), l)       # E
    l = h(M, (x, y+1), l)       # S

    if C == l:
        return l
    else:
        return g(M, l)

def f(M):
    ret = []
    for j in range(len(M)):
        r = []
        for i in range(len(M[0])):
            r.append(g(M, (i, j)))
        ret.append(r)
    return ret

def solve(inp):
    T = int(inp.pop(0))

    for n in range(T):
        (H, W) = map(int, inp.pop(0).split(" "))

        M = []
        for _ in range(H):
            M.append(list(map(int, inp.pop(0).split(" "))))

        print("Case #%s:" % str(n+1))
        printmap(j(f(M)))

def printmap(M):
    for row in M:
        for cell in row:
            print(cell, end=" ")
        print()

def file_as_list(filename):
    with open(filename) as f:
        lst = []
        for ln in f:
            lst.append(ln[:-1])
        return lst

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print("Usage: %s input" % sys.argv[0])
    else:
        solve(file_as_list(sys.argv[1]))
