from math import sqrt
import re
import sys

def is_fs(case):
    start, end = get_values(case)
    return str(count_fs_in_interval(start, end))

def count_fs_in_interval(start,end):
    n = 0
    for i in range(start, end+1):
        if is_fair_and_square(i):
            n += 1
    return n

def get_values(case):
    n = case.split()
    assert len(n) == 2
    return (int(n[0]), int(n[1]))

def is_palidrome(n):
    number = str(n)
    if len(number) == 1:
        return True
    elif len(number) % 2 == 0:
        p2 = number[len(number)/2:][::-1]
    else:
        p2 = number[len(number)/2 + 1:][::-1]
    p1 = number[0:len(number)/2]
    return p1 == p2

def is_integer(n):
    if n % 2 == 0 or (n + 1)%2 == 0:
        return True
    return False

def is_square(n):
    nn = sqrt(n)
    if is_integer(nn):
        return is_palidrome(int(nn))
    return False

def is_fair_and_square(n):
    if is_square(n) and is_palidrome(n):
        return True
    return False

def report(case):
    m = re.match(r'^(\d+)\n', case)
    n = int(m.group(0))
    case = re.sub(r'^(\d+)\n', '', case)
    data = case.strip().split('\n')
    assert n == len(data), 'Error size %d != %d' % (n, len(data))
    output = []
    for i,c in enumerate(data):
        output.append('Case #%d: %s' % (i+1, is_fs(c)))
    return '\n'.join(output)

def main(args, dry = False):
    if len(args) > 1:
        f = open(args[1])
        data = f.read()
        f.close()
        output = report(data)
        if dry:
            return output
        f = open(args[1] + '.output','w')
        f.write(output)
        f.close()

if __name__ == '__main__':
    main(sys.argv)