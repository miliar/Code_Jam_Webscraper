def flip(p):
    return '+' if p == '-' else '-'


def flipLine(line):
    return ''.join([flip(p) for p in line])


fOut = open('A-small-test.out', 'w')
with open('A-small-test.in') as fin:
    num = int(fin.readline().strip())  # number of test cases

    for testcase in range(0, num):
        pancakes, k = fin.readline().strip().split()
        k = int(k)
        flips = 0
        for i in range(0, len(pancakes) - k + 1):
            p = pancakes[i]
            if p == '+':
                continue
            else:  # flip
                flips += 1
                updatedPancakes = pancakes[:i] + flipLine(pancakes[i : i + k]) + pancakes[i + k:]
                pancakes = updatedPancakes
        res = "IMPOSSIBLE" if '-' in pancakes else str(flips)
        fOut.write('Case #%i: %s\n' % (testcase + 1, res))
fOut.close()