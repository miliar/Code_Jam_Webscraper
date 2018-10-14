# by Enrique Gonzalez (Enriikke)
# enjoy!

import math

# Setup the files here.
in_file = '../../../Downloads/C-small-attempt0.in'
out_file = 'solution.out'
try:
    in_file = open(in_file, 'r')
    out_file = open(out_file, 'w')
except IOError as e:
    print e.errno
    print e.strerror


# Quick util function to print out a single case solution.
def print_solution(case_number, solution, file=out_file):
    try:
        file.write('Case #{0!s}: {1}\n'.format(case_number, solution))
    except Exception as e:
        print type(e)
        print e.args


# This is just a place holder and it makes it easier to read the code.
def parse_data(file=in_file):
    A, B = file.readline().split()
    A = int(math.ceil(math.sqrt(int(A))))
    B = int(math.floor(math.sqrt(int(B))))
    
    return A, B


def solve_it():
    # Number of test cases
    N = int(in_file.readline())
    
    # Iterate through every test case
    for n in range(1, N + 1):
        # Get my case data ready
        A, B = parse_data()
        
        # Magic goes here
        solution = ''
        fair_square_count = 0
        for i in range (A, B + 1):
            square = str(i * i)
            is_palindrome = str(i) == str(i)[::-1]
            if is_palindrome and square == square[::-1]: 
                fair_square_count = fair_square_count + 1
        
        solution = str(fair_square_count)
        
        # Print solution
        print_solution(n, solution)
    
    
    # Close both files
    in_file.close()
    out_file.close()


solve_it()
