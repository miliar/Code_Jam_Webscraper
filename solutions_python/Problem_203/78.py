#!/usr/bin/env python2
import itertools
def solve_row(prev_row, row):
    prev_row = list(prev_row)
    prev_chars = set(prev_row)
    #print prev_row, row
    for i, row_i in enumerate(row):
        if row_i == '?':
            continue
        min_i = i
        max_i = i
        while max_i + 1 < len(prev_row) and prev_row[max_i] == prev_row[max_i + 1]:
            max_i += 1
        while min_i - 1 >= 0 and prev_row[min_i] == prev_row[min_i - 1] and prev_row[min_i] in prev_chars:
            min_i -= 1
        prev_row[min_i:max_i+1] = row_i * (max_i + 1 - min_i)
    return prev_row
def solve(r, c, a):
    ans = []
    prev_row = ['?' for _ in a[0]]
    for row in a:
        if any(row_i != '?' for row_i in row):
            prev_row = solve_row(prev_row, row)
            break 
    for row in a:
        prev_row = solve_row(prev_row, row)
        ans.append(prev_row)
    assert '?' not in prev_row
    return ans
def _iter_tuples(a):
    for i, row in enumerate(a):
        for j, row_j in enumerate(row):
            yield i, j, row_j
def _to_tuples(a):
    return list(_iter_tuples(a))
def check(r, c, a, ans):
    a = _to_tuples(a)
    ans = _to_tuples(ans)
    for (i, j, char) in a:
        if char != '?':
            assert (i, j, char) in ans
    ptslen = 0
    for char in {char for (i, j, char) in a}:
        if char == '?':
            continue
        pts = {(i, j) for (i, j, char2) in ans if char2 == char}
        ptslen += len(pts)
        i_min = min(i for i, j in pts)
        i_max = max(i for i, j in pts)
        j_min = min(j for i, j in pts)
        j_max = max(j for i, j in pts)
        pts2 = {(i, j) for i in xrange(i_min, 1 + i_max) for j in xrange(j_min, 1 + j_max)}
        assert pts == pts2, (char, pts2 - pts)
    assert ptslen == r * c
def main():
    for t in xrange(1, 1 + int(raw_input())):
        print 'Case #%d:' % t
        r, c = map(int, raw_input().split())
        a = [list(raw_input().strip()) for _ in xrange(r)]
        ans = solve(r, c, a)
        check(r, c, a, ans)
        for row in ans:
            print ''.join(row)
if __name__ == '__main__':
    main()
