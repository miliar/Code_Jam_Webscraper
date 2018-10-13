import sys

def solve():
    line = [int(x) for x in sys.stdin.readline().strip().split(" ")]
    n, s, p = line[0:3]
    meja = 3*p-2 if p >= 1 else 0
    bonusMeja = 3*p-4 if p >= 2 else p
    cnt = 0
    for t in line[3:]:
        if t >= meja:
            # print("acc:", t)
            cnt += 1
        elif t >= bonusMeja and s > 0:
            # print("bonus:", t)
            cnt += 1
            s -= 1
    return cnt

T = int(sys.stdin.readline())
for testCase in range(1, T+1):
    print("Case #%i:" % testCase, solve())
