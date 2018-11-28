import itertools
from collections import OrderedDict
PROBLEM_ID = "B" # A B or C
PROBLEM_SIZE = "small"

def run():
    """I/O handler"""
    file_name = "{}-{}".format(PROBLEM_ID, PROBLEM_SIZE)
    in_f = open('{}.txt'.format(file_name), 'r')
    out_f = open('{}.out'.format(file_name), 'w')
    num_of_case = int(in_f.readline().rstrip('\n'))
    print "num of cases:{}".format(num_of_case)
    for i in range(1, num_of_case+1):
        solve_case(in_f, out_f, i)

def solve_case(in_f, out_f, case_index):
    """problem solver"""
    print "case #{}:".format(case_index)
    N = int(in_f.readline().rstrip('\n'))
    cars = map(remove_ad, in_f.readline().rstrip('\n').split(" "))
    print cars
    
    # get permutations:
    perms = itertools.permutations(cars, N)
    total = 0
    for pp in perms:
        pps = "".join(pp)
        if is_valid(pps):
            total += 1
    print total
    # get the solution 

    # write the solution   
    out_f.write("Case #{}: {}\n".format(case_index, total))

def is_valid(s):
    # remove dup
    current = ''
    seen = set()
    for l in s:
        if l != current:
            if l in seen:
                return False
            seen.add(l) # TODO: might use dic
            current = l
    return True       

def remove_ad(s):
    # remove dup
    current = ''
    ss = ""
    for l in s:
        if l != current:
            current = l
            ss += l
    return ss       


run()
