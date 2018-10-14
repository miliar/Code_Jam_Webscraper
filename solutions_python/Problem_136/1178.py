from decimal import *

T = int(input())
format_string = "Case #{0}: {1}"
SEVENPLACES = Decimal(10) ** -7

for i in range(T):
    string = input()
    tuples = tuple(float(x) for x in string.strip().split(" "))
    C, F, X = tuples
    rate = 2
    time = 0

    while True:
        no_factory = X / rate
        factory = C / rate + X / (rate + F)

        if factory < no_factory:
            time += C / rate
            rate += F
        else:
            time += X / rate
            break


    print(format_string.format(i+1, Decimal(str(time)).quantize(SEVENPLACES)))
