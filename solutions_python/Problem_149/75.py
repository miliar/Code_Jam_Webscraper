import Queue
import copy

def ok(S):
    i = 0
    while i + 1 < len(S) and S[i] < S[i + 1]:
        i += 1
    while i + 1 < len(S) and S[i] > S[i + 1]:
        i += 1
    if i == len(S) - 1:
        print S
        return True
    else:
        return False

def solve():
    N = int(raw_input())
    S = map(int, raw_input().split())
    sorted_S = sorted(S)
    count = 0
    for v in sorted_S:
        index = 0
        i = 0
        left_edge = -1
        left = 0
        while S[i] != v:
            if S[i] > v:
                left += 1
                if left_edge == -1:
                    left_edge = i
            i += 1
        index = i
        right_edge = -1
        right = 0
        while i < len(S):
            if S[i] > v:
                right += 1
                right_edge = i
            i += 1
        if left == 0 or right == 0:
            continue
        if left < right:
            count += index - left_edge
            S.pop(index)
            S.insert(left_edge, v)
        else:
            count += right_edge - index
            S.insert(right_edge + 1, v)
            S.pop(index)
    return count

T = int(raw_input())
for i in range(T):
    print 'Case #%d:' % (i + 1), solve()
