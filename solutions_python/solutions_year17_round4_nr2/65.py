#!/usr/bin/env python

import sys

def solve():
    N, C, M = [int(i) for i in raw_input().split()]
    seats = [0] * N
    customers = [0] * C
    for _ in xrange(M):
        seat, customer = [int(i) for i in raw_input().split()]
        customers[customer-1] += 1
        seats[seat-1] += 1
    customer_rides = max(customers)
    cumm_seats = [0]
    for v in seats:
        cumm_seats.append(v + cumm_seats[-1])
    cumm_seats.pop(0)
    seat_rides = max(v/(k+1) + (v % (k+1) > 0) for k, v in enumerate(cumm_seats))
    max_rides = max(customer_rides, seat_rides)
    i = upgrades = 0
    for j in xrange(N):
        if seats[j] > max_rides:
            extra_seats = seats[j] - max_rides
            seats[j] = max_rides
            while extra_seats > 0:
                if i >= j:
                    sys.exit("Inconceivable")
                if seats[i] < max_rides:
                    s = min(max_rides - seats[i], extra_seats)
                    upgrades += s
                    seats[i] += s
                    extra_seats -= s
                    if extra_seats == 0:
                        break
                i += 1
    return "{} {}".format(max_rides, upgrades)


def main():
    T = int(raw_input())
    for i in xrange(T):
        sol = solve()
        print 'Case #{}: {}'.format(i+1, sol)


if __name__ == '__main__':
    main()
