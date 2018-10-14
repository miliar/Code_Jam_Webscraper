from decimal import *

T = int(raw_input())

for i in xrange(0, T):
    getcontext().prec = 7

    l = map(float, raw_input().split())
    C = l[0]
    F = l[1]
    X = l[2]

    total = 0
    income = 2
    future_income = 2 + F
    new_farm_time = C/income


    while total + new_farm_time + X/future_income < total + X/income:
        total += new_farm_time
        income = future_income
        future_income = income + F
        new_farm_time = C/income
            
    total += X/income

    print "Case #{}: {}".format(i+1, total)
