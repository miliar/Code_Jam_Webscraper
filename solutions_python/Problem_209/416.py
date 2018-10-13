def solve(line):
    n, k = map(int, line.split())
    r = [0 for i in range(n)]
    h = [0 for i in range(n)]
    for i in range(n):
        r[i], h[i] = map(int, sys.stdin.readline().rstrip().split())
    an = sorted([(2 * r[i] * h[i], i) for i in range(n)], key=lambda x: x[0], reverse=True)
    final = 0
    for ind1 in range(n):
        result = r[ind1] ** 2 + 2 * r[ind1] * h[ind1]
        dn = [i[1] == ind1 for i in an[0:k]]
        if any(dn):
            result = max([r[i[1]] for i in an[0:k]]) ** 2 + sum([i[0] for i in an[0:k]])
        else:
            result += sum([i[0] for i in an[0:k - 1]])
        if result > final:
            final = result
    return final * math.pi
