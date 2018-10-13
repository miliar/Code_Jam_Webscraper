import itertools
import math


def count1():
    cnt = 0
    for j in range(P):
        num0 = Q[0][j] / R[0]
        if round(num0) * 0.9 <= num0 <= round(num0) * 1.1:
            cnt += 1
    return cnt


def count2(item):
    # Q[2]とitemのセットでRとのきっと作成できるかどうか問題
    cnt = 0
    for i in range(P):
        if ok(item[i], Q[1][i]):
            cnt += 1
    return cnt


def ok(q0, q1):
    num0 = q0 / R[0]
    if not (round(num0) * 0.9 <= num0 <= round(num0) * 1.1):
        return False
    sita = math.ceil(num0 / 1.1)
    ue = math.floor(num0 / 0.9)
    if q1 / 1.1 <= sita * R[1] <= q1 / 0.9:
        return True
    if q1 / 1.1 <= ue * R[1] <= q1 / 0.9:
        return True
    return False


def solve():
    cnt = -1
    if N == 1:
        cnt = count1()
        pass
    if N == 2:
        for item in itertools.permutations(Q[0]):
            cnt = max(cnt, count2(item))
    return cnt


if __name__ == '__main__':
    T = int(input())
    for t in range(1, T + 1):
        N, P = map(int, input().split())
        R = list(map(int, input().split()))
        Q = [list(map(int, input().split())) for _ in range(N)]
        ret = solve()
        print("Case #{x}: {y}".format(x=t, y=ret))