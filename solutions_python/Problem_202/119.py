#!/usr/bin/python3

import sys, datetime

def solve(n, m, p):
    cols = {}
    for x, i, j in p:
        cols[j] = x
    added = []
    if n not in cols or cols[n] == '+':
        if 'x' not in cols.values() and 'o' not in cols.values():
            added.append(('o', 1, 1))
            for j in range(2, n + 1):
                if j not in cols:
                    added.append(('+', 1, j))
                added.append(('x', j, j))
                if j < n:
                    added.append(('+', n, j))
        else:
            i = 2
            for j in range(1, n + 1):
                if j not in cols:
                    added.append(('+', 1, j))
                elif cols[j] == 'x':
                    added.append(('o', 1, j))
                if j not in cols or cols[j] == '+':
                    added.append(('x', i, j))
                    i += 1
                if 1 < j < n:
                    added.append(('+', n, j))
    else:
        if cols[n] == 'x':
            added.append(('o', 1, n))
        for j in range(1, n):
            if j not in cols:
                added.append(('+', 1, j))
            added.append(('x', n + 1 - j, j))
            if j > 1:
                added.append(('+', n, j))
    ret = "%d %d" % (3*n - 2 if n > 1 else 2, len(added))
    for x, i, j in added:
        ret += '\n' + "%s %d %d" % (x, i, j)
    return ret

def parse(input_file):
    n, m = map(int, input_file.readline().strip().split())
    p = []
    for i in range(m):
        x, r, c = input_file.readline().strip().split()
        p.append((x, int(r), int(c)))
    return (n, m, p)

def main():
    start = datetime.datetime.now()
    input_file = open(sys.argv[1])
    output_file = open(sys.argv[2], "w") if len(sys.argv) > 2 else None
    print("Writing to %s" % sys.argv[2] if output_file else "No output file")
    test_cases = int(input_file.readline().strip())
    print("Test cases:", test_cases)
    print('-----------------')
    for tc in range(1, test_cases + 1):
        output = "Case #%d: %s" % (tc, solve(*parse(input_file)))
        print(output)
        if output_file:
            output_file.write(output + "\n")
    print('-----------------')
    print("Written to %s" % sys.argv[2] if output_file else "No output file")
    print('Elapsed time: %s' % (datetime.datetime.now() - start))
    input_file.close()
    if output_file:
        output_file.close()

if __name__ == "__main__":
    main()
