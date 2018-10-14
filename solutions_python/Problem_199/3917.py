#!/usr/bin/env python3

T = int(input())

def filp(c) :
    if c == '+':
        return '-'
    else:
        return '+'

def filp_range(idx):
    global K, S
    # print(''.join(S), end=' to ')
    for i in range(idx, idx+K):
            S[i] = filp(S[i])
    # print(''.join(S))

def is_happy():
    return all(tuple(map(lambda x: x == '+', S)))

for test in range(1, T+1):
    cnt, min_cnt = 0, 987654321
    S, K = input().split()
    S = [c for c in S]
    K = int(K)
    

    def select_pancake(idx):
        global cnt, min_cnt

        if idx + K > len(S):
            return
        # print(idx, ''.join(S))
        # print('try:',end=' ')
        filp_range(idx)
        cnt += 1
        if is_happy():
            min_cnt = min(cnt, min_cnt)
        select_pancake(idx+1)
        cnt -= 1

        # print('rollback:',end=' ')
        filp_range(idx)

        select_pancake(idx+1)

    if is_happy():
        print('Case #{}: {}'.format(test, 0))
        continue

    select_pancake(0)
    if min_cnt != 987654321:
        print('Case #{}: {}'.format(test, min_cnt))
    else:
        print('Case #{}: {}'.format(test, 'IMPOSSIBLE'))






