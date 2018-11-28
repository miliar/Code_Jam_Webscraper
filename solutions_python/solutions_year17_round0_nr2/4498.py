def solve(n):
    lst = [int(i) for i in str(n)]
    sol = 0
    for i in reversed(range(1, len(lst))):
        if lst[i] < lst[i - 1]:
            lst[i-1] -= 1
            for j in range(i, len(lst)):
                lst[j] = 9
    val = ""
    if lst[0] == 0:
        lst = lst[1:]
    for i in lst:
        val += str(i)
    return val


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n = int(input())
    print("Case #{}: {}".format(i, solve(n)))
