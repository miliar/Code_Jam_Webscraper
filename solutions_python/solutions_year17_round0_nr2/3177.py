def solve_test(inp, out):
    n = list(map(int, list(inp.readline().strip())))
    was = True
    while was:
        was = False
        for i in range(len(n) - 1):
            if n[i] > n[i + 1]:
                n[i] -= 1
                for j in range(i + 1, len(n)):
                    n[j] = 9
                was = True
                break
    print(int(''.join(map(str, n))), file=out)


def run():
    with open('B-large.in') as inp, open('B-large.out', 'w') as out:
        tests = int(inp.readline())
        for i in range(tests):
            print(i)
            print("Case #%d: " % (i + 1), file=out, end='')
            solve_test(inp, out)
if __name__ == '__main__':
    run()