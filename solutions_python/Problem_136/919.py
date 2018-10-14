#!/usr/bin/python
import sys

def solve(C, F, X):
    total_time = 0.0
    prod_rate = 2.0
    while True:
        time_a = X / prod_rate
        time_b = (C / prod_rate) + (X / (prod_rate + F))
        #print "C=%f, F=%f, X=%f, total_time=%f, prod_rate=%f, time_a=%f, time_b=%f" % (C, F, X, total_time, prod_rate, time_a, time_b)
        if time_a < time_b:
            return (total_time + time_a,)
        else:
            total_time += (C / prod_rate)
            prod_rate += F

def parse_case(*args):
    C, F, X = map(float, R().split())
    return (C, F, X)

def format_ret(ret):
    return "%.7f" % ret

def R(cast = None):
    ret = sys.stdin.readline().strip()
    if cast is not None:
        ret = cast(ret)
    return ret

def W(msg, *args):
    sys.stdout.write((msg + "\n") % args)

def main():
    cases = R(int)
    for i in range(1,cases+1):
        ret = solve(*parse_case())
        W("Case #%d: %s", i, format_ret(*ret))

if __name__ == '__main__':
    main()
