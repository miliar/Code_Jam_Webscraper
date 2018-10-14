
def main(C, F, X):
    rate = 2
    time = 0
    max_rate = F*X/C
    while rate+F < max_rate:
        time += C/rate
        rate += F
    time += X/rate

    return round(time, 7)

assert main(500, 4, 2000) == 526.1904762

n_lines = int(input())
for i in range(n_lines):
    print("Case #{}: {}".format(1+i, main(*[float(num) for num in input().split()])))
