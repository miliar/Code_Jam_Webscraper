def search_tail(s, C, L, rep = 1):
    for i in xrange(s, C):
        temp = "".join(L[i])
        if temp != '?' * len(temp):
            return i
    return C


def sol_line(C, L):
    head = -1
    tail = search_tail(0, C, L)
    for i in xrange(C):
        if L[i] == '?':
            if tail < C:
                L[i] = L[tail]
            else:
                L[i] = L[head]
        else:
            head = i
            tail = search_tail(i + 1, C, L)


def sol(R, C, M):
    head = -1
    tail = search_tail(0, R, M, C)
    if tail < R:
        sol_line(C, M[tail])
    for i in xrange(R):
        if M[i] == ['?'] * C:
            if tail < R:
                M[i] = M[tail]
            else:
                M[i] = M[head]
        else:
            head = i
            tail = search_tail(i + 1, R, M, C)
            if tail < R:
                sol_line(C, M[tail])
            sol_line(C, M[i])
    result = ""
    for i in xrange(R - 1):
        result += "".join(M[i]) + "\n"
    result += "".join(M[-1])
    return result

if __name__ == "__main__":
    t = long(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        line = raw_input()
        R, C = line.split()
        R = int(R)
        C = int(C)
        M = []
        for j in xrange(R):
            line = raw_input()
            M.append(map(lambda x: x, line))
        print "Case #{}:\n{}".format(i, sol(R, C, M))
