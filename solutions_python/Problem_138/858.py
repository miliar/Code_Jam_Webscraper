import sys
import time
import math

def solve_case(case):
    naomi = [(float(x),'n') for x in case[0].split()]
    ken = [(float(x),'k') for x in case[1].split()]
    both = naomi + ken
    both.sort(key=lambda x:x[0], reverse=True)
    n = 0
    k = 0
    for _, n_or_k in both:
        if n_or_k == 'n':
            if k == 0:
                n += 1
            else:
                k -= 1
        else:
            k += 1
    both.reverse()
    y = len(naomi)
    k = 0
    for _, n_or_k in both:
        if n_or_k == 'n':
            if k == 0:
                y -= 1
            else:
                k -= 1
        else:
            k += 1
    return "%d %d" % (y, n)

def get_case(file_obj):
    ignored_N = file_obj.next()
    return [ file_obj.next(), file_obj.next() ]

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
