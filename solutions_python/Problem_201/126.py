#!/usr/bin/python3

import sys, datetime

def solve(n, k):
    d = {n: 1}
    while k:
        m = max(d)
        l = d[m]
        a = (m - 1)//2
        b = a + (m - 1)%2
        if k <= l:
            return "%d %d" % (b, a)
        del d[m]
        if a not in d:
            d[a] = 0
        if b not in d:
            d[b] = 0
        d[a] += l
        d[b] += l
        k -= l

def parse(input_file):
    n, k = map(int, input_file.readline().strip().split())
    return (n, k)

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
