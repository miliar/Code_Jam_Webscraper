import sys
import time
import math

def solve_case(case):
    c, f, x = (float(i) for i in case.rstrip().split())
    n = 1.0
    s = 1.0/2
    pre = x/2.0
    while True:
        takes = x/(2+f * n) + c * s
        if takes > pre:
            break
        pre = takes
        s += 1/(2+f*n)
        n += 1
    return "%.7f" % ( pre,)

def get_case(file_obj):
    return file_obj.next()

def read_input():
    file_name = sys.argv[1]
    file_obj = open(file_name, "r")
    number_of_cases = int(file_obj.next().rstrip())
    return number_of_cases, file_obj

def main():
    number_of_cases, file_obj = read_input()
    output_file_name = "output_%s.txt" % (time.strftime("%Y-%m-%d-%H-%M-%S"),)
    output_obj = open(output_file_name, "w")
    cases = []
    for i in xrange(0,number_of_cases):
        case = get_case(file_obj)
        result = solve_case(case)
        output_obj.write("Case #%d: %s\n" % (i+1, str(result)))
        output_obj.flush()
main()
