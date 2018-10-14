import math
import bisect

def bullseye():
    """
        used to solve google code jam 2013 Round 1A - Problem A
    """
    in_f = open('A-small-attempt1.in', 'r')
    out_f = open('A-small-attempt1.out', 'w')
    num_of_case = int(in_f.readline().rstrip('\n'))
    print "num of cases:{}".format(num_of_case)
    for i in range(1, num_of_case+1):
        solve_case(in_f, out_f, i)
        
def solve_case(in_f, out_f, case_index):
    """
    solve each case
    """
    print "start handling case #{}".format(case_index)
    #
    
    bound_info = in_f.readline().rstrip('\n').split(" ")
    r = int(bound_info[0])
    t = int(bound_info[1])
    y_max = math.sqrt((4*r*r - 4*r + 1)/16.0 + t/2.0) + (1 - 2*r)/4.0
    print y_max
    out_f.write("Case #{}: {}\n".format(case_index, int(y_max)))

        
if __name__ == '__main__':    
    bullseye()

