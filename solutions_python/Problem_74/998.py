#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from collections import defaultdict

def solve_case(orders):
    """
    orders - lista par (korytarz - litera O/B, przycisk - int)
    """
    orange_spent = 0
    black_spent = 0
    orange_position = 1
    black_position = 1

    for corridor, target in orders:
        if corridor == 'O':
            # Chodzimy swobodnie
            orange_spent += abs(orange_position - target)
            orange_position = target
            # Naciskamy dopiero po poprzedniku
            if orange_spent < black_spent:
                orange_spent = black_spent
            # Naciskamy
            orange_spent += 1
        else:
            # Chodzimy swobodnie
            black_spent += abs(black_position - target)
            black_position = target
            # Naciskamy dopiero po poprzedniku
            if black_spent < orange_spent:
                black_spent = orange_spent
            # Naciskamy
            black_spent += 1

    return max(orange_spent, black_spent)

def parse_case(case_line):
    items = case_line.replace("\n", "").split(" ")
    orders_count = int(items[0])
    orders = [
        (items[1 + 2*x],
         int(items[2 + 2*x]))
        for x in range(0, orders_count) ]
    return orders

if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = sys.argv[0].replace(".py", ".in")
    input = open(filename)
    outputname = filename.replace(".in",".out")
    output = open(outputname, "w")

    print "Converting %s to %s" % (filename, outputname)

    cases_count = int(input.readline())
    for case_no in xrange(1, cases_count+1):
        reply = solve_case(parse_case(input.readline()))
        txt = "Case #%d: %d\n" % (
            case_no, reply)
        output.write(txt)
        print txt,

    output.close()
    input.close()

