'''
Created on April 12, 2014

@author: Lior
'''


def solve(n):
    for i in range(len(n)-1):
        if n[i] <= n[i+1]:
            continue
        n = n[:i] + str(int(n[i])-1) + "9"*len(n[i+1:])
        return solve(n)
    return n


def process_files(in_file, out_file):
    num_of_test_cases = int(in_file.next().strip())
    i = 0
    for line in in_file:
        i += 1
        n = line.strip()
        result = solve(n).lstrip('0')
        out_file.write("Case #" + str(i) + ": " + result + "\n")

if __name__ == '__main__':
    import sys, os
    in_file = sys.argv[1]
    out_file = in_file.replace('.in', '.out')
    with open(in_file, 'rb') as in_file:
        with open(out_file, 'wb') as out_file:
            process_files(in_file, out_file)
