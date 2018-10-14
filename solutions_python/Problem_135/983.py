"""Solve Code Jam Qualifying Round Problem A.

Reads input from stdin.
"""

import fileinput

def main():
    """Main program execution steps.

    """
    # read all input data into a list and reverse it to make it easy
    # to pop off.
    input_data = []
    for line in fileinput.input():
        input_data.append(line.strip())
    input_data = input_data[::-1] # reverse list

    # number of input cases
    num_cases = int(input_data.pop())

    for i in range(num_cases):
        # parse the data and solve each case inline
        first_choice = int(input_data.pop())
        first_grid = []
        # extract grid lines for first grid
        for j in range(4):
            line = [int(num) for num in input_data.pop().split(' ')]
            first_grid.append(line)
        second_choice = int(input_data.pop())
        second_grid = []
        # extract grid lines for second grid
        for j in range(4):
            line = [int(num) for num in input_data.pop().split(' ')]
            second_grid.append(line)
        # solve this case
        solve_case(first_choice, first_grid,
                   second_choice, second_grid, i + 1)        


def solve_case(first_choice, first_grid,
               second_choice, second_grid,
               case_num):
    """Solve an instance of the magician's problem.

    For brevity, also emits the output, though this would typically be
    performed separately.
    
    """
    poss = set(first_grid[first_choice-1])
    poss = poss.intersection(set(second_grid[second_choice-1]))
    output_string_parts = ['Case #' + str(case_num) + ':']
    if len(poss) == 0:
        output_string_parts.append('Volunteer cheated!')
    elif len(poss) == 1:
        output_string_parts.append(str(list(poss)[0]))
    else:
        output_string_parts.append('Bad magician!')
    print ' '.join(output_string_parts)


if __name__ == "__main__":
    main()
