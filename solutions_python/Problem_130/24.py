def HighestPlace(k, N):
    upper = 0
    lower = 0
    same_upper = k
    same_lower = 2 ** N - 1 - k
    for i in range(N):
        if same_lower == 0:
            return upper + same_upper
        else:
            total = 1 + same_upper + same_lower
            lower += 1
            same_lower -= 1
            if same_lower % 2 == 0:
                lower += same_lower // 2
                same_lower //= 2
                lower += same_upper // 2
                same_upper //= 2
            else:
                lower += (same_lower + 1) // 2
                same_lower //= 2
                lower += same_upper // 2
                same_upper = (same_upper + 1) // 2
    return upper + same_upper

def LowestPlace(k, N):
    upper = 0
    lower = 0
    same_upper = k
    same_lower = 2 ** N - 1 - k
    for i in range(N):
        if same_upper > 0:
            same_upper -= 1
            upper += 1
            if same_upper % 2 == 0:
                upper += same_upper // 2
                same_upper //= 2
                upper += same_lower // 2
                same_lower //= 2
            else:
                upper += (same_upper + 1) // 2
                same_upper //= 2
                upper += same_lower // 2
                same_lower = (same_lower + 1) // 2
        else:
            return upper
    return upper

def solve(num):
    N, P = map(int, input().split())
    ans1 = 0
    ans2 = 2 ** N - 1
    for i in range(2 ** N):
        # print("Team", i, "Highest", HighestPlace(i, N), "Lowest", LowestPlace(i, N))
        if LowestPlace(i, N) < P:
            ans1 = i
        if HighestPlace(i, N) < P:
            ans2 = i
    print("Case #", num, ": ", ans1, " ", ans2, sep='')

T = int(input())
for num in range(1, T + 1):
    solve(num)

