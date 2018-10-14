def is_tidy(n):
    string = str(n)
    return (string == "".join(sorted(list(string))))

def solve(n):
    for i in range(n, 0, -1):
        if is_tidy(i):
            return i
    return 0

T = int(input())
for i in range(1, T+1):
    solution = solve(int(input()))
    print("Case #{}: {}".format(i, solution))
