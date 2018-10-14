import sys


SUP = 1000000000


#cin = open('input.txt', 'r')
#cin = open('B-small-attempt0.in', 'r')
cin = open('B-large.in', 'r')
#cin = sys.stdin
cout = open('output.txt', 'w')
#cout = sys.stdout

current_str_iter = None


def next_token():
    global current_str_iter

    while True:
        if current_str_iter is not None:
            token = next(current_str_iter, None)
            if token is not None:
                return token

        current_str_iter = iter(cin.readline().split())


def next_int():
    return int(next_token())


def solve(n, p, reqs, q):
    ranges = []
    for i in range(n):
        q[i] = sorted(q[i])
        ranges.append([])

        for j in range(p):
            lb = (10 * q[i][j]) / (reqs[i] * 11)
            if (10 * q[i][j]) % (reqs[i] * 11) > 0:
                lb += 1

            rb = (10 * q[i][j]) / (reqs[i] * 9)

            if rb >= lb:
                ranges[i].append((lb, rb))

    indices = []
    for i in range(n):
        indices.append(0)

    result = 0
    while indices[0] < len(ranges[0]):
        if rec(0, -1, SUP, n, ranges, indices) == -1:
            result += 1

    return result


def rec(v, lb, rb, n, ranges, indices):
    if v == n:
        return -1

    while indices[v] < len(ranges[v]) and ranges[v][indices[v]][1] < lb:
        indices[v] += 1

    if indices[v] == len(ranges[v]):
        return SUP

    if ranges[v][indices[v]][0] > rb:
        return ranges[v][indices[v]][0]

    newlb = max(lb, ranges[v][indices[v]][0])
    newrb = min(rb, ranges[v][indices[v]][1])

    result = rec(v + 1, newlb, newrb, n, ranges, indices)

    if result == -1:
        indices[v] += 1
    else:
        while indices[v] < len(ranges[v]) and ranges[v][indices[v]][1] < result:
            indices[v] += 1

    return result


def main():
    testcases = next_int()

    for tc in range(1, testcases + 1):
        n = next_int()
        p = next_int()

        reqs = []
        for i in range(n):
            reqs.append(next_int())

        q = []
        for i in range(n):
            q.append([])
            for j in range(p):
                q[i].append(next_int())

        result = solve(n, p, reqs, q)

        cout.write('Case #%i: %s\n' % (tc, str(result)))


if __name__ == '__main__':
    main()