from fractions import Fraction as frac

def solve():
    c, f, x = map(float, raw_input().split(" "))
    
    rate = 2.0
    time = c / rate

    while (x / (rate + f)) < (x - c) / rate:
        rate += f
        time += c / rate

    time += (x - c) / rate

    return time

cases = int(raw_input())

for case in range(cases):
    answer = solve()
    print "Case #{}: {}".format(case + 1, answer)