import csv
import os
import sys

def solve(N, K):
    nb = 2**N
    if K % nb == nb - 1:
        return "ON"
    else:
        return "OFF"

def main(src, dst):
    reader = csv.reader(src, delimiter=" ")

    T = int(reader.next()[0])

    for t in range(T):
        N, K = map(int, reader.next())
        answer = solve(N, K)
        dst.write("Case #%d: %s\n" % (t + 1, answer))

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
