import sys


def read(f):
    with open(f) as file:
        lines = file.readlines()
    T = int(lines[0])
    for x, t in enumerate(range(1, T+1)):
        N, K = lines[t].split()
        y, z = solve(int(N), int(K))
        print('Case #%i: %s %s' % ((x+1), y, z))


def solve(N, K):
    L = [-1]
    L.extend([0]*N)
    L.extend([-1])
    for k in range(K):  # For each person k
        z, y = find_pos(L, N)
    return y, z


def find_pos(L, N):
    Li = [0]*(N+2)
    Ri = [0]*(N+2)

    def from_left(A):
        j = 0  # Bathroom guard on the left
        for i in range(1, len(L)-1):
            A[i] = i - j - 1
            if L[i] == -1:
                j = i
        return A

    def from_right(A):
        j = len(L) - 1  # Bathroom guard on the right
        for i in range(1, len(L)-1):
            i = len(L) - i - 1
            A[i] = j - i - 1  # len(L)-1-len(L)+2-1 => 0
            if L[i] == -1:
                j = i
        return A

    Li = from_left(Li)
    Ri = from_right(Ri)

    c1_list = []
    c1 = -1
    for s in range(1, len(L)-1):
        if L[s] == -1:
            continue

        c1_s = min(Li[s], Ri[s])
        if c1_s > c1 or c1 == -1:
            c1 = c1_s
            c1_list = [s]
        elif c1_s == c1:
            c1_list.append(s)

    if len(c1_list) == 1:
        assert L[c1_list[0]] != -1
        L[c1_list[0]] = -1
        return min(Li[c1_list[0]], Ri[c1_list[0]]), max(Li[c1_list[0]], Ri[c1_list[0]])
    else:
        assert L[c1_list[0]] != -1
        c2_list = [c1_list[0]]
        c2 = max(Li[c1_list[0]], Ri[c1_list[0]])
        for s in c1_list[1:]:
            if L[s] == -1:
                continue

            c2_s = max(Li[s], Ri[s])
            if c2_s > c2:
                c2 = c2_s
                c2_list = [s]
            elif c2_s == c2:
                c2_list.append(s)

        assert L[c2_list[0]] != -1
        L[c2_list[0]] = -1
        return min(Li[c2_list[0]], Ri[c2_list[0]]), max(Li[c2_list[0]], Ri[c2_list[0]])

read(sys.argv[1])
