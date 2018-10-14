#!/usr/bin/python

import sys

def war(idx, first_list, second_list):
    """docstring for war"""
    #print first_list
    #print second_list
    N = len(first_list)
    war_count = [0] * N
    i = N - 1
    j = N - 1
    while i >=0 and j>=0:
        if first_list[i] > second_list[j]:
            war_count[j] += 1
            i -= 1
        else:
            j -= 1
            if j >= 0:
                war_count[j] = war_count[j+1]
    if i < 0 and j >=0:
        for k in range(j):
            war_count[k] = war_count[j]
    #print war_count
    for i in range(N):
        war_count[i] = war_count[i] - (N - i - 1)
    final_war_count = max(war_count)
    
    cheat_count = [0] * N
    i = 0
    j = 0
    while i < N and j < N:
        if second_list[j] < first_list[i]:
            cheat_count[i] += 1
            j += 1
        else:
            i += 1
            if i < N:
                cheat_count[i] = cheat_count[i - 1]
    if j >= N and i < N:
        for k in range(i+1, N):
            cheat_count[k] = cheat_count[i]
    for i in range(N):
        cheat_count[i] = cheat_count[i] - (i + 1)
    tmp = min(cheat_count)
    if tmp < 0:
        final_cheat_count = N + tmp
    else:
        final_cheat_count = N
    print "Case #%d: %d %d" % (idx, final_cheat_count, final_war_count)


def main():
    """entry point"""
    input = sys.stdin.readlines()
    case_num = int(input[0])
    for i in range(case_num):
        first_list = [float(val) for val in input[3*i + 2].strip().split()]
        second_list = [float(val) for val in input[3*i + 3].strip().split()]
        first_list.sort()
        second_list.sort()
        war(i+1, first_list, second_list)


if __name__ == '__main__':
    main()
