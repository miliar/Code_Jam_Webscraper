"""
if everyone had one pancake, then that would be the fastest possible

there's a tension between getting all pancakes distributed evenly and
taking time to move some pancakes from one diner's plate to another

the minutes breakfast takes is the sum of the max number of pancakes consumed
by a diner plus the number of special minutes
"""

PRIMES = (2, 3)


def memo(f):
    """memoization decorator, taken from Peter Norvig's Design of Computer
    Programs course on Udacity.com"""
    cache = {}
    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            result = cache[args] = f(*args)
            return result
        except TypeError:  # unhashable argument
            return f(*args)
    return _f


def apply_regular_minute(plates):
    regular_move = (p - 1 for p in plates)
    return (p for p in regular_move if p > 0)


def apply_special_minute(plates, tallest, n_non_empty, prime_divisors):
    max_pancakes = plates[tallest]
    removals = (max_pancakes / d for d in prime_divisors)
    for r in removals:
        yield ((max_pancakes - r) if i == tallest
               else r             if i == n_non_empty
               else plates[i]
               for i in xrange(n_non_empty + 1))


@memo
def solve(plates):
    "return the minimum number of minutes breakfast can take"
    n_non_empty = len(plates)

    if n_non_empty == 0:
        return 0

    # regular minute
    regular_minutes = solve(tuple(apply_regular_minute(plates)))

    # special minute
    tallest = max((i for i in xrange(n_non_empty)), key=lambda i: plates[i])
    max_pancakes = plates[tallest]
    prime_divisors = tuple(p for p in PRIMES if max_pancakes % p ==0)
    if max_pancakes <= 1 or len(prime_divisors) == 0:
        # no need to divide pancakes
        special_minutes = solve(tuple(apply_regular_minute(plates)))
    else:
        special_minutes = min(solve(tuple(p))
                              for p in apply_special_minute(plates,
                                                            tallest,
                                                            n_non_empty,
                                                            prime_divisors))

    # take minutes from shortest path
    return 1 + min(regular_minutes, special_minutes)


def std_in():
    while True:
        yield raw_input()


def main():
    STD_IN = std_in()

    T = int(next(STD_IN).strip())

    for t in xrange(T):
        _ = next(STD_IN)
        plates = tuple(map(int, next(STD_IN).strip().split()))
        solution = solve(plates)
        print 'Case #{}: {}'.format(t+1, solution)


if __name__ == '__main__':
    main()
