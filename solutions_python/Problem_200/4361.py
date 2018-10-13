def tidy(c):
    return str(c) == "".join(sorted(list(str(c))))

def solve(m):
    power = 0
    while not tidy(m):
        if str(m)[::-1][power]== "9":
            power +=1
        else:
            m = m - 10**power
    return m

t = int(input())
for i in range(1, t + 1):
    n = int(input())
    res = solve(n)
    print("Case #{}: {}".format(i, res))