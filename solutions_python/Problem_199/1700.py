#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
# vi: set fileencoding=utf-8 :


def flip(S, K, i):
    for j in range(K):
        if S[i + j] == '-':
            S[i + j] = '+'
        else:
            S[i + j] = '-'
    return


def solve(S, K):
    flip_num = 0
    for i in range(len(S) - K + 1):
        if S[i] == '-':
            flip(S, K, i)
            flip_num += 1
    for s in S[-K+1:]:
        if s == '-':
            return 'IMPOSSIBLE'
    return str(flip_num)


T = int(input())
for case_number in range(1, T + 1):
    S, K = input().split()
    K = int(K)
    S = list(S)
    print('Case #%d: %s' % (case_number, solve(S, K)))
