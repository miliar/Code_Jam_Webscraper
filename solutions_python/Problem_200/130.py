#!/usr/bin/python3

import sys, datetime

def solve(n):
    l = list(map(int, str(n)))
    i = 0
    while i < len(l) - 1 and l[i] <= l[i + 1]:
        i += 1
    if i == len(l) - 1:
        return n
    while i > 0 and l[i - 1] == l[i]:
        i -= 1
    return int(''.join(map(str, l[:i])) + str(l[i] - 1) + '9'*(len(l) - i - 1))

def parse(input_file):
    n = int(input_file.readline().strip())
    return (n,)

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
