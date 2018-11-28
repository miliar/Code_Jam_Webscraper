#!/usr/bin/python3

import sys

nRounds = int(sys.stdin.readline().strip())

for _ in range(0, nRounds):
    sys.stdout.write("Case #{}: ".format(_+1))
    strInput = sys.stdin.readline().strip().split(' ')
    # do something
    n_seats  = int(strInput[0])
    n_cust   = int(strInput[1])
    n_ticket = int(strInput[2])
    customers = [0] * n_cust
    positions = [0] * n_seats

    for i in range(0,n_ticket):
        strInput = sys.stdin.readline().strip().split(' ')
        pos   = int(strInput[0])
        buyer = int(strInput[1])
        customers[buyer-1] += 1
        positions[pos-1] += 1
    max_customer = max(customers)
    max_round = 0
    sum_now = 0
    for i in range(0, n_seats):
        sum_now += positions[i]
        need_round = (sum_now + i) // (i+1)
        max_round = max(max_round, need_round)
    max_round = max(max_round, max_customer)
    need_promote = 0
    for i in range(0, n_seats):
        need_promote += max(0, positions[i] - max_round)
    sys.stdout.write('{} {}'.format(max_round, need_promote))
    sys.stdout.write("\n")
    sys.stdout.flush()
