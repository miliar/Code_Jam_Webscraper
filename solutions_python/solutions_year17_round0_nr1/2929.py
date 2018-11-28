def solve_test(inp, out):
    line, k = inp.readline().split()
    line = [1 if x == '+' else 0 for x in list(line)]
    k = int(k)
    ans = 0
    for i in range(len(line) - k + 1):
        if line[i] == 0:
            ans += 1
            for j in range(i, i + k):
                line[j] = 1 - line[j]
    for i in range(len(line) - k + 1, len(line)):
        if line[i] == 0:
            print('IMPOSSIBLE', file=out)
            return
    print(ans, file=out)


def run():
    with open('A-large.in') as inp, open('A-large.out', 'w') as out:
        tests = int(inp.readline())
        for i in range(tests):
            print(i)
            print("Case #%d: " % (i + 1), file=out, end='')
            solve_test(inp, out)
if __name__ == '__main__':
    run()