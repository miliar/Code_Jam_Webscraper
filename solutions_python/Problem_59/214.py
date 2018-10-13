import array
import csv
import os
import sys


def make_dirs(paths, root):
    n_mkdir = 0
    for p in paths:
        cwd = root
        for n in p.split("/")[1:]:
            if n not in cwd:
                cwd[n] = {}
                n_mkdir += 1
            cwd = cwd[n]
    return n_mkdir


def solve(paths, new_paths):
    n_mkdir = 0
    root = {}
    _ = make_dirs(paths, root)
    answer = make_dirs(new_paths, root)
    
    return answer

def main(src, dst):
    reader = csv.reader(src, delimiter=" ")

    T = int(reader.next()[0])

    for t in range(T):
        N, M = map(int, reader.next())
        paths = set()
        new_paths = set()
        for n in range(N):
            paths.add(reader.next()[0])
        for m in range(M):
            new_paths.add(reader.next()[0])

        answer = solve(paths, new_paths)
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
