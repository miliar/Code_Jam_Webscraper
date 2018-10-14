import sys
import time
import math

def solve_case(case):
    first_ans = int(case[0].rstrip())
    first_row = case[first_ans].rstrip().split()
    second_ans = int(case[5].rstrip())
    second_row = case[5+second_ans].rstrip().split()
    ans = set(first_row).intersection(set(second_row))
    if len(ans) == 0:
        return "Volunteer cheated!"
    elif len(ans) > 1:
        return "Bad magician!"
    else:
        return list(ans)[0]

def get_case(file_obj):
    case = []
    for i in xrange(0, 1 + 4 + 1 + 4):
        case.append( file_obj.next() )
    return case

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
