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


def solve(N, K, B, T, xlist, vlist):
    clist = zip(xlist, range(N), vlist)
    clist.sort(reverse=True)

    tlist = []
    n_swap = 0
    n_can_arrive = 0 
    if K == 0:
        return 0
    
    for x, _, v in clist:
        t = float((B - x)) / float(v)
        tlist.append(t)

        if t <= T:
            n_can_arrive += 1

    if n_can_arrive < K:
        return "IMPOSSIBLE"

    n_arrive = 0
    for idx in range(N):
        if tlist[idx] <= T:
            n_swap += idx - n_arrive
            n_arrive += 1
        if n_arrive == K:
            return str(n_swap)

    return "IMPOSSIBLE"

def main(src, dst):
    reader = csv.reader(src, delimiter=" ")

    C = int(reader.next()[0])

    for t in range(C):
        N, K, B, T = map(int, reader.next())
        xlist = map(int, reader.next())
        vlist = map(int, reader.next())
        answer = solve(N, K, B, T, xlist, vlist)
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
