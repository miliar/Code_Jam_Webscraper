from decimal import Decimal

cases = int(raw_input())

n = cases

results = []

while n > 0:
    seconds = []

    C, F, X = map(Decimal, raw_input().split(' '))

    current_C = Decimal(0.0)
    producing = Decimal(2.0)

    while True:
        def time_if_buy(F, X, producing):
            return X / (producing + F)

        buy_another_in = C / producing
        time_to_win = X / producing

        if_buy = time_if_buy(F, X, producing)

        if (if_buy + buy_another_in) < time_to_win:
            producing += F
            seconds.append(buy_another_in)
        else:
            current_C += producing * time_to_win
            seconds.append(time_to_win)

        if abs(current_C - X) <= Decimal('0.00000001'):
            results.append(reduce(lambda x, y: x + y, seconds))
            break

    n -= 1

for i in range(cases):
    print 'Case #%d: %s' % (i + 1, str(results[i]))
