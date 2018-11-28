# Codejam 2014 Qualifiers - B: Cookie Clicker Alpha

def solve(n):
    total = 0
    for x in range(n):
        total += C / (2.0 + x * F)
    total += X / (2.0 + n * F)
    return total

with open("B-large.in", "rU") as f:
##with open("cookieClicker.in", "rU") as f:
    with open("B-large.out", "w") as output:
        for curr_case in range(1, int(f.readline()) + 1):
            # C cost of farm, F farm production rate, X cookie goal
            C, F, X = map(float, f.readline().strip().split())
            if C >= X:
                answer = solve(0)
            else:
##                answer = solve(int(X / C) - 1)
                n = 1
                low, high = solve(0), solve(1)
##                while high < low and n <= int(X / C) + 2:
##                    n += 1
##                    low = high
##                    high = solve(n)
                while high < low and n <= int(X / C) + 2:
                    low = high
                    high += (C - X) / (2.0 + n * F) + X / (2.0 + (n + 1) * F)
                    n += 1
                answer = min(low, high)
            print("Case #{}: {:.7f}".format(curr_case, answer))
            output.write("Case #{}: {:.7f}\n".format(curr_case, answer))
