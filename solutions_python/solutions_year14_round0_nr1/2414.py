'''
Qualification Round 2014, A - Magic Trick.
'''

import sys

def read_test_case_arrangment(lines):

    answer = int(lines[0])
    grid = []
    for i in xrange(1,5):
        grid.append([int(n) for n in lines[i].split()])


    print 'answer:', answer
    print 'grid:', grid

    return answer, grid

def read_test_case(lines):
    
    a = read_test_case_arrangment(lines[:5])
    b = read_test_case_arrangment(lines[5:10])

    return a, b

def solve_test_case(test_case):

    a, b = test_case
    a_answer = a[0]
    a_grid   = a[1]
    a_row    = a_grid[a_answer - 1]
    b_answer = b[0]
    b_grid   = b[1]
    b_row    = b_grid[b_answer - 1]

    print a_row, b_row
    s = set(a_row).intersection(b_row)
    length = len(s)
    res = ''
    if length == 0:
        res = "Volunteer cheated!"
    elif length > 1:
        res = "Bad magician!"
    else:
        res = str(list(s)[0])

    return res

def main():

    input_path = sys.argv[1]
    output_path = sys.argv[1].replace('.in', '.out')
    input_lines = open(input_path, 'rb').readlines()
    output_file = open(output_path, 'w')
    
    number_of_cases = int(input_lines[0])
    for i in xrange(number_of_cases):

        # handle case
        k = 1 + 10 * i
        test_case = read_test_case(input_lines[k:k + 10])
        result = solve_test_case(test_case)

        output_file.write("Case #%d: %s\n" % (i + 1, result))

if __name__=='__main__':
    main()
