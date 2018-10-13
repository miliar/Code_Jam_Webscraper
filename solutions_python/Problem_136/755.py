from decimal import Decimal, ROUND_HALF_UP
from itertools import count
from sys import stdin


# the rate at which cookies are gained
R = Decimal('2.0')


input_it = iter(stdin)

T = int(input_it.next())

for t in range(T):

    # interpret input
    C, F, X = (Decimal(c) for c in input_it.next().split())


    _time_to_n_farms_cache = {0: Decimal('0')}
    def time_to_n_farms(n):
        """ Returns (time in seconds, remaining cookies) """
        if n not in _time_to_n_farms_cache:
            _time_to_n_farms_cache[n] = time_to_n_farms(n - 1) + C / (R + (n - 1) * F)
        return _time_to_n_farms_cache[n]


    y = X / R
    for n in count(1):
        y_new = time_to_n_farms(n) + X / (R + n * F)
        if y < y_new: break
        else: y = y_new


    print 'Case #{t}: {y}'.format(t=t+1, y=y.quantize(Decimal('.0000001'), rounding=ROUND_HALF_UP))
