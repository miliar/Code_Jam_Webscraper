from collections import defaultdict
import copy

def valid_packs(v, r):
    ratio = v / r
    valid = set()
    for p in range(int(np.floor(ratio/1.1)), 1 + int(np.ceil(ratio/0.9))):
        if p * 0.9 <= ratio <= p * 1.1:
            valid.add(p)
    return valid

def helper(q, mini, minlen):
    result = 0
    if minlen == 0:
        return result
    while len(q[mini]) > 0:
        possible_ps = q[mini].pop()
        for p in possible_ps:
            tempq = copy.deepcopy(q)
            valid = True
            for i in range(len(tempq)):
                if i == mini:
                    continue
                found = False
                for j in range(len(tempq[i])):
                    if p in tempq[i][j]:
                        del tempq[i][j]
                        found = True
                        break
                if not found:
                    valid = False
            if valid:
                result += 1
                break
    return result

def solve2(n, p, lines):
    r = [int(i) for i in lines[0].split()]
    q = []
    for i, l in enumerate(lines[1:]):
        tmp = []
        for v in map(int, l.split()):
            packages = valid_packs(v, r[i])
            if len(packages) > 0:
                tmp.append(packages)
        q.append(tmp)
    minlen, mini = len(q[0]), 0
#     print(r, q)
    for i in range(1, n):
        if len(q[i]) < minlen:
            minlen, mini = len(q[i]), i
    return helper(q, mini, minlen)

with open('out2', 'wt') as o:
    lines = [l.strip() for l in open('B-small-attempt0.in').readlines()]
    numTests = int(lines[0])
    nextTestLine = 1
    testsCounter = 0
    while testsCounter < numTests:
        testsCounter += 1
        n, p = [int(i) for i in lines[nextTestLine].split()]
        testLines = lines[nextTestLine + 1 : nextTestLine + 1 + n + 1]
        nextTestLine += n + 1 + 1
        print('\nsolving: n=%s p=%s, lines=\n%s' % (n, p, '\n'.join(testLines)))
        res = solve2(n, p, testLines)
        result = 'Case #%d: %s' % (testsCounter, res)
        print(result)
        _ = o.write(result + '\n')

