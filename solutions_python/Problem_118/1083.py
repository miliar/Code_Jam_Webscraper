import math

def fair_and_square():
    """
        used to solve google code jam 2013 - Problem C
    """
    in_f = open('C-small-attempt0.in', 'r')
    out_f = open('C-small-attempt0_output.txt', 'w')
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
    min = int(bound_info[0])
    max = int(bound_info[1])
    print (min, max)
    total_fair_and_square = 0
    for j in range(min, max+1):
        # todo: try switch this two to see the efficiency differences
        if is_square_and_square_root_palindrome(j) and is_palindrome(j):
            total_fair_and_square = total_fair_and_square + 1
            print j
    print "total:{}".format(total_fair_and_square)
    out_f.write("Case #{}: {}\n".format(case_index, total_fair_and_square))

def is_square_and_square_root_palindrome(int_value): 
    """
    return True if int_value is square and square root is palindrome
    """
    root = math.sqrt(int_value)
    int_root = int(root)
    if int_root == root:
        return is_palindrome(int_root)
    return False

def is_palindrome(int_value): 
    """
    return True if int_value is palindromeI
    """
    str_value = str(int_value)
    reversed_str = str_value[::-1]
    return reversed_str == str_value

if __name__ == '__main__':
    fair_and_square()

