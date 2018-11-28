def solve():
    D,N = list(map(int, input().split()))
    slow = -1
    for _ in range(N):
        h,s = list(map(int, input().split()))
        slow = max((D - h) / s, slow)
    return D / slow

t = int(input())
for i in range(t):
    print("Case #{0}:".format(i+1), solve())
