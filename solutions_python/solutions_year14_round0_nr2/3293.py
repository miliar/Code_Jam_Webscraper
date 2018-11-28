import sys
import math

def get_input():
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
        if filename != '-':
            return open(filename)
    return sys.stdin

def print_case(i,result):
    print "Case #%s: %s" % (i,result)

def time_to_goal(goal, farm_prod, num_farms):
    return goal / (2 + farm_prod*num_farms)

def read_case(inp):
    return [float(val) for val in inp.readline().strip().split(" ")]

def get_time(C,F,X):
    total_time = 0
    for num_farms in xrange(int(math.ceil(X))):
        tf = time_to_goal(C,F,num_farms)
        tg = time_to_goal(X,F,num_farms)
        tgf = time_to_goal(X,F,num_farms+1)
        if tg <= tf + tgf:
            total_time += tg
            break
        else:
            total_time += tf
    return total_time

if __name__ == "__main__":
    src = get_input()
    cases = int(src.readline())
    for i in xrange(1,cases+1):
        C, F, X = read_case(src)

        total_time = get_time(C,F,X)
        print_case(i,"%.7f" % total_time)