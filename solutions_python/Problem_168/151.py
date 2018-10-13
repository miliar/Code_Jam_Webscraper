#!/usr/bin/python

def solve(A):
    h_borders = []
    for i in xrange(r):
        min_c, max_c = None, None
        for j in xrange(c):
            if A[i][j] != ".":
                if min_c is None:
                    min_c = j
                max_c = j
        h_borders.append((min_c, max_c))

    v_borders = []
    for j in xrange(c):
        min_r, max_r = None, None
        for i in xrange(r):
            if A[i][j] != ".":
                if min_r is None:
                    min_r = i
                max_r = i
        v_borders.append((min_r, max_r))

    result = 0
    for i in xrange(r):
        for j in xrange(c):
            if (h_borders[i][1] == j and
                h_borders[i][0] == j and
                v_borders[j][1] == i and
                v_borders[j][0] == i):
                return "IMPOSSIBLE"
            if A[i][j] == ">":
                if h_borders[i][1] == j:
                    result+= 1
            elif A[i][j] == "<":
                if h_borders[i][0] == j:
                    result+= 1
            elif A[i][j] == "v":
                if v_borders[j][1] == i:
                    result+= 1
            elif A[i][j] == "^":
                if v_borders[j][0] == i:
                    result+= 1

    return result



if __name__ == '__main__':
    T = int(raw_input())
    for t in range(T):
        r, c = map(int, raw_input().split())
        A = []
        for i in xrange(r):
            A.append(raw_input().strip())
        answer = solve(A)
        print "Case #{0}: {1}".format(t + 1, answer)
