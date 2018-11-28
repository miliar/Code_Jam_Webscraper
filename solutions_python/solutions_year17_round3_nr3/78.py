import sys
import bisect


def answer(N, K, U, probs):

    if N == 1:
        return probs[0] + U

    probs = sorted(probs)
    probs.append(1.0)
    prices = []

    for i in range(len(probs)-1):
        prices.append((i+1)*(probs[i+1] - probs[i]))


    cum_prices = []
    cum_price = 0.0
    cum_prices.append(0.0)
    for price in prices:
        cum_prices.append(cum_price + price)
        cum_price += price

    if cum_prices[-1] <= U:
        return 1.0


    for i, total_price in enumerate(cum_prices):
        if total_price <= U:
            continue
        else:
            for j in range(i-1):
                probs[j] = probs[i-1]
            remaining_capacity = U - cum_prices[i-1]
            for j in range(i):
                probs[j] += remaining_capacity / (i + 0.0)
            break

    assert max(probs) <= 1.0

    result = reduce(lambda x, y: x*y, probs, 1.0)

    return result



if __name__ == "__main__":

    T = int(sys.stdin.next())
    queries = []
    for i in range(T):
        N, K = map(int, sys.stdin.next().split(' '))
        u, = map(float, sys.stdin.next().split(' '))
        probs = map(float, sys.stdin.next().split(' '))

        queries.append((N, K, u, probs))
    for i, q in enumerate(queries):
        print "".join(["Case #", str(i + 1), ": ", str(round(answer(*q), 8))])

