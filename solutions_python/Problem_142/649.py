# -*- coding: utf-8 -*-
'''
'''
import sys
sys.stdin = open('A-small-attempt1.in')

cases = int(input())
for case_num in range(cases):

    n = int(input())

    strings = []
    for x in range(n):
        strings.append(input())

    char_permutation = []
    char_occur_num = []
    for line in strings:
        occurence = ['']
        occur_num = [0]
        for x in line:
            if occurence[-1] != x:
                occurence.append(x)
                occur_num.append(1)
            else:
                occur_num[-1] += 1
        char_permutation.append(occurence)
        char_occur_num.append(occur_num)
    
    possible = (char_permutation[1:] == char_permutation[:-1])
    if possible:
        modify_need = 0
        for idx in range(len(char_occur_num[0])):
            occur_num_col = [x[idx] for x in char_occur_num]
            average = round(sum(occur_num_col) / len(occur_num_col))
            #most_frequent = max(set(occur_num_col), key=occur_num_col.count)
            for row in occur_num_col:
                modify_need += abs(average - row)
        result = modify_need
    else:
        result = 'Fegla Won'

    print('Case #{}: {}'.format(case_num + 1, result))
