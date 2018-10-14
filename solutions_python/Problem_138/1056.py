#!/usr/bin/env python3
# encoding: utf-8

import bisect as b


cases = int(input())

for case in range(cases):
    blocks = int(input())
    blocks_n = sorted([float(i) for i in input().split()])
    blocks_k = sorted([float(i) for i in input().split()])
    blocks_n_dw = list(blocks_n)
    blocks_k_dw = list(blocks_k)

    # play WAR
    score_w = 0
    while len(blocks_n) > 0:
        # find the first block gratest then the one selected by naomy
        tell_k = blocks_n[0]
        idx = b.bisect(blocks_k, tell_k)
        if (idx == len(blocks_k)):
            # didn't find any match, use minimum
            idx = 0
        if blocks_n[0] > blocks_k[idx]:
            score_w += 1
        # delete used blocks
        del blocks_n[0], blocks_k[idx]
    # play D.WAR
    score_dw = 0
    while len(blocks_n_dw) > 0:
        idx_n = b.bisect(blocks_n_dw, blocks_k_dw[0])
        tell_k = blocks_k_dw[-1] + 1e-6
        if (idx_n == len(blocks_n_dw)):
            # didn't find any match, use minimum
            idx_n = 0
            tell_k = blocks_n_dw[idx_n]
        idx_k = b.bisect(blocks_k_dw, tell_k)
        if (idx_k == len(blocks_k_dw)):
            # didn't find any match, use minimum
            idx_k = 0
        if tell_k > blocks_k_dw[idx_k]:
            score_dw += 1
        # delete used blocks
        del blocks_n_dw[idx_n], blocks_k_dw[idx_k]
    print('Case #{}: {} {}'.format(case + 1, score_dw, score_w))
