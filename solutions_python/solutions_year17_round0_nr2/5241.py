import sys

T = int(sys.stdin.readline())

for t in range(1, T+1):
    n = int(sys.stdin.readline())
    ans = 0
    for i in range(1, n+1):
        digits = [int(x) for x in str(i)]
        flag = True
        for d in range(len(digits)-1):
            if digits[d] > digits[d+1]:
                flag = False
                break
        if flag:
            ans = i
    print('Case #{}: {}'.format(t, ans))
