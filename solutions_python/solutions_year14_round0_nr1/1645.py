# This is just a starter file for other problems
# I like making this readble so you might see some extra steps
#
# by Enrique Gonzalez (Enriikke)
# enjoy!


############### FILE NAMES ###############
input = 'A-small-attempt0.in'
output = 'data.out'



# Open (create) the files needed to read the data and write the solution.
def open_files(input, output):
    try:
        input_file = open(input, 'r')
        output_file = open(output, 'w')

        return input_file, output_file

    except Exception as e:
        print type(e)
        print e.args



# Quick util function to print out a single case solution.
def print_solution(case_number, solution, file):
    try:
        file.write('Case #{0!s}: {1}\n'.format(case_number, solution))

    except Exception as e:
        print type(e)
        print e.args



# Read the data for a single case from the input file.
def parse_data(file):
    try:
        case_data = []
        for i in xrange(2):
          row_num = int(file.readline())
          for l in xrange(4):
            if l+1 == row_num:
              case_data.append(file.readline().split())
            else:
              file.readline()

        return case_data[0], case_data[1]

    except Exception as e:
        print type(e)
        print e.args



# Solve the problem!!
def solve():
    # Open the files needed.
    input_file, output_file = open_files(input, output)

    # Get the total number of cases.
    total_cases = int(input_file.readline())
    for case in xrange(1, total_cases + 1):

        #Get the case data.
        first_row, second_row = parse_data(input_file)

        # Do all the magic here.
        possible_cards = set(first_row) & set(second_row)
        cards_count = len(possible_cards)

        solution = ''
        if cards_count == 1:
          solution = possible_cards.pop()
        elif cards_count == 0:
          solution = 'Volunteer cheated!'
        else:
          solution = 'Bad magician!'


        # Print solution to file.
        print_solution(case, solution, output_file)


    # Close the files used.
    input_file.close()
    output_file.close()



#import cProfile
#cProfile.run('solve()')
solve()
