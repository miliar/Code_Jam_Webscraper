#!/usr/bin/env python3

for t in range(int(input())):
    seats, customers, tickets = map(int, input().split())
    count = [0] * seats
    holded = [0] * customers
    for _ in range(tickets):
        s, c = map(int, input().split())
        count[s - 1] += 1
        holded[c - 1] += 1
    lb = max(holded)
    for i in range(seats):
        lb = max(lb, (count[i] + i) // (i + 1))
    pro = 0
    for c in count:
        pro += max(c - lb, 0)
    print('Case #{}: {} {}'.format(t + 1, lb, pro))
