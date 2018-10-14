#!/usr/bin/python

import sys

def is_possible(hgrid, v_num, h_num):
    vgrid = [list(i) for i in zip(*hgrid)]
    for v in xrange(v_num):
        for h in xrange(h_num):
            if hgrid[v][h] < max(hgrid[v]) and vgrid[h][v] < max(vgrid[h]):
                return False
    return True

def main():
    for tc_num in xrange(int(sys.stdin.readline())):
        v_num, h_num = (int(i) for i in sys.stdin.readline().split())
        grid = [sys.stdin.readline().split() for _ in xrange(v_num)]
        print "Case #%d: %s" % (tc_num + 1, "YES" if is_possible(grid, v_num, h_num) else "NO")

if __name__ == "__main__":
    main()
