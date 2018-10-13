#!/usr/bin/python3

import sys, datetime

def solve(s, k):
    s = list(map(lambda x:1 if x == '+' else 0, s))
    c = 0
    for i in range(len(s) - k + 1):
        if s[i] == 0:
            for j in range(i, i + k):
                s[j] = (s[j] + 1)%2
            c += 1
    if 0 in s:
        return 'IMPOSSIBLE'
    return c

def parse(input_file):
    s, k = input_file.readline().strip().split()
    return (s, int(k))

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
