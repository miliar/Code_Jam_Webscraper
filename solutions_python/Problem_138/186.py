import copy

PROBLEM_ID = "D" # A B or C
PROBLEM_SIZE = "large"

def run():
    """
        I/O handler
    """
    file_name = "{}-{}".format(PROBLEM_ID, PROBLEM_SIZE)
    in_f = open('{}.txt'.format(file_name), 'r')
    out_f = open('{}.out'.format(file_name), 'w')
    num_of_case = int(in_f.readline().rstrip('\n'))
    print "num of cases:{}".format(num_of_case)
    for i in range(1, num_of_case+1):
        solve_case(in_f, out_f, i)

def solve_case(in_f, out_f, case_index):
    """
        problem solver
    """
    print "case #{}".format(case_index)
    in_f.readline()
    A = [float(x) for x in in_f.readline().rstrip('\n').split(" ")]
    B = [float(x) for x in in_f.readline().rstrip('\n').split(" ")]
    total_tile = len(A)
    A.sort()
    A.reverse()
    B.sort()
    B.reverse()
    A1 = copy.copy(A)
    B1 = copy.copy(B)
    # start deceitful war
    DWP = total_tile - game(B1, A1)
    # start war
    WP = game(A, B)
             
    out_f.write("Case #{}: {} {}\n".format(case_index, DWP, WP))

def game(A, B): # return game result of A in favor of B
    AW = 0
    BW = 0
    while len(A) > 0:
        if B[0] > A[0]: # win one!
            BW += 1
            B.pop(0)
            A.pop(0)
        else: # there is no equal, throw smallest one
            AW += 1
            A.pop(0)
            B.pop(-1)
    return AW
    
        
#    out_f.write("Case #{}: {}\n".format(case_index, "Bad magician!"))

#. if has bigger, use lowest-bigger one.
#  else, discard lowest one.


# use the smallest one to pretend to be just a little bit smaller than Dan's to destroy Dan's biggest one.
# stop until all the ones are bigger than dan's



run()
