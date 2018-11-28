import csv
import operator
import os
import sys

D = 21
assert 2**(D-1) - 10**6 > 0

def solve(values):
    nlist = [0] * D

    for v in values:
        w = format(v, 'b').zfill(D)
        for i, b in enumerate(w[::-1]):
            if b == '1':
                nlist[i] += 1

    p = reduce(operator.and_, [n % 2 == 0  for n in nlist])

    if p:
        values.sort()
        return sum(values[1:])
    else:
        return 'NO'


def main(src, dst):
    reader = csv.reader(src, delimiter=" ")

    T = int(reader.next()[0])

    for t in range(T):
        N = int(reader.next()[0])
        values = map(int, reader.next())

        assert N == len(values)

        answer = solve(values)
        dst.write("Case #%d: %s\n" % (t + 1, answer))

    assert src.read() == ""

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "Usage: python solve.py input output"
        raise SystemExit

    src_path = os.path.abspath(sys.argv[1])
    src = open(src_path, "r")

    
    dst_path = os.path.abspath(sys.argv[2])
    if os.path.exists(dst_path):
        print "already exists: %s" % dst_path
        raise SystemExit
    dst = open(dst_path, "w")

    try:
        main(src, dst)
    finally:
        src.close()
        dst.close()
