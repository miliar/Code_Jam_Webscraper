#!/usr/bin/env python

import sys

def main():
    cin = sys.stdin
    num_tests = int(cin.readline())
    for test_id in range(1, num_tests + 1):
        rows, cols = map(int, cin.readline().split())
        lawn = []
        for _ in range(rows):
            lawn.append(map(int, cin.readline().split()))
            assert(cols == len(lawn[-1]))
        row_maxs = []
        for row in lawn:
            row_maxs.append(max(row))
        col_maxs = []
        for j in range(cols):
            col_maxs.append(max([lawn[i][j] for i in range(rows)]))
        consistent = True
        for i in range(rows):
            for j in range(cols):
                if lawn[i][j] >= row_maxs[i] or lawn[i][j] >= col_maxs[j]:
                    continue
                consistent = False
                break
        print "Case #%d: %s" % (test_id, "YES" if consistent else "NO")

if __name__ == "__main__":
    main()
