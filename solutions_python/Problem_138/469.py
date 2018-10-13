#!/usr/bin/env python

import sys
from copy import copy


def main():
    T = int(sys.stdin.readline())
    for t in range(1, T+1):
        N = int(sys.stdin.readline().strip())
        naomi = sorted(map(float, sys.stdin.readline().strip().split()))
        ken = sorted(map(float, sys.stdin.readline().strip().split()))
        war_naomi = copy(naomi)
        war_ken = copy(ken)
        war_score_n, war_score_k = 0, 0
        #print N, naomi, ken
        for x in war_naomi:
            k = 0
            flag = False
            for y in war_ken:
                if y > x:
                    k = y
                    war_score_k += 1
                    flag = True
                    break
            if not flag:
                k = war_ken[0]
                war_score_n += 1
            war_ken.remove(k)
            #print x, ' vs. ', k

        dec_naomi = copy(naomi)
        dec_ken = copy(ken)
        seq = []
        dec_score_n, dec_score_k = 0, 0
        #print dec_naomi
        #print dec_ken
        i, j = 0, 0
        while i < len(dec_naomi) and j < len(dec_ken):
            if dec_naomi[i] < dec_ken[j]:
                seq.append('n')
                i += 1
            else:
                seq.append('k')
                j += 1
        if i < len(dec_naomi) and j == len(dec_ken):
            for ii in range(len(dec_naomi) - i):
                seq.append('n')
        elif i == len(dec_naomi) and j < len(dec_ken):
            for jj in range(len(dec_ken) - j):
                seq.append('k')
        #print seq

        seq_str = ''.join(seq)
        while len(seq_str) > 0:
            #print seq_str, seq_str[0]
            if seq_str[0] == 'n':
                idx = seq_str.rfind('k')
                seq_str = seq_str[1:idx] + seq_str[idx+1:]
                dec_score_k += 1
            elif seq_str[0] == 'k':
                idx = seq_str.find('n')
                seq_str = seq_str[1:idx] + seq_str[idx+1:]
                dec_score_n += 1

        print "Case #" + str(t) + ": " + \
              str(dec_score_n) + " " + str(war_score_n)


if __name__ == '__main__':
    main()
