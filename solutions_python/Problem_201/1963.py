T = int(input())

def solution():
    n, k = map(int, input().split())
    lst = [1] + [0] * n + [1]
    for iteration in range(k):
        closest_right = [n + 1] * (n + 2)
        closest_left = [0] * (n + 2)
        for i in range(1, n + 2):
            closest_left[i] = i if lst[i] else closest_left[i - 1]
        for i in range(n, -1, -1):
            closest_right[i] = i if lst[i] else closest_right[i + 1]
        best = (-float("inf"), -float("inf"))
        t = 0
        for i in range(1, n + 1):
            if lst[i]:
                continue
            mn = min(i - closest_left[i] - 1, closest_right[i] - i - 1)
            mx = max(i - closest_left[i] - 1, closest_right[i] - i - 1)
            if (mn, mx) > best:
                best = (mn, mx)
                t = i
        lst[t] = 1
        #print(lst)
    return reversed(best)




for test in range(1, T + 1):
    print("Case #{}: {} {}".format(test, *solution()))