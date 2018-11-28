import sys, os, re, collections

def print_result (case_num, result):
    print('Case #{}: {}'.format(case_num + 1, result))


for case_num in range(int(input())):
    S,K = input().split()
    K = int(K)
    S = list(S)
    result = 0
    assert K >= 2
    for i in range(len(S[:-K+1])):
        if S[i] == '-':
            result += 1
            for j in range(i,i+K):
                S[j] = '+' if S[j] == '-' else '-'
    if all([p == '+' for p in S]):
        print_result(case_num,result)
    else:
        print_result(case_num,'IMPOSSIBLE')
