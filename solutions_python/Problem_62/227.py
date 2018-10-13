import array
import csv
import os
import logging
import sys

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def solve(wire_list):
    wire_list.sort()

    d = {}
    n_intersect = 0

    for a, b in wire_list:
        d[b] = 0
        for wire_end in d:
            if b < wire_end:
                n_intersect += 1

    return n_intersect

def main(src, dst):
    reader = csv.reader(src, delimiter=" ")

    T = int(reader.next()[0])

    for t in range(T):
        N = map(int, reader.next())[0]
        wire_list = []
        for n in range(N):
            wire_list.append(map(int, reader.next()))

        answer = solve(wire_list)
        dst.write("Case #%d: %d\n" % (t + 1, answer))

    assert src.read() == ""

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Usage: python solve.py input output"
        raise SystemExit

    src_path = os.path.abspath(sys.argv[1])
    src = open(src_path, "r")

    if len(sys.argv) == 2:
        dst = sys.stdout
    else:
        dst_path = os.path.abspath(sys.argv[2])
        if os.path.exists(dst_path):
            raise ValueError("already exists: %s" % dst_path)
        dst = open(dst_path, "w")

    try:
        main(src, dst)
    finally:
        src.close()
        dst.close()
