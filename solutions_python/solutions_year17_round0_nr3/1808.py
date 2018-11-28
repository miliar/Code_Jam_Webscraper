#coding: utf-8
import sys
INPUT_FILE = 'C-small-1-attempt0.in'
OUTPUT_FILE = 'C-small-1-attempt0.out'
sys.stdin = file(INPUT_FILE, 'r')
sys.stdout = file(OUTPUT_FILE, 'w')


T = int(raw_input())
for case in xrange(1, T+1):
    N, K = map(int, raw_input().split())
    occupied = [0, N+1]
    # init
    ans = -1
    for i in range(K):
        tmp_lst = []
        sentinel = -1
        seq = sorted(occupied)
        for j in range(len(seq)-1):

            begin, end = seq[j]+1, seq[j+1]-1
            for k in range(begin, end+1):
                Ls, Rs = k-begin, end-k
                if min(Ls, Rs) > sentinel:
                    ans = (k, max(Ls, Rs), min(Ls, Rs))
                    sentinel = min(Ls, Rs)
                    tmp_lst = [(max(Ls, Rs), min(Ls, Rs), k)]
                elif min(Ls, Rs) == sentinel:
                    tmp_lst.append((max(Ls, Rs), min(Ls, Rs), k))
        if len(tmp_lst) != 1:
            sentinel = -1
            for vmax, vmin, k in tmp_lst:
                if vmax > sentinel:
                    sentinel = vmax
                    ans = (k, vmax, vmin)
        occupied.append(ans[0])
    print 'Case #%d: %d %d' % (case, ans[1], ans[2])






