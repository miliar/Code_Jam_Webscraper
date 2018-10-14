'''
Created on Apr 12, 2014

@author: learning-python
'''

def get_choices (row_zero_index, grid):
    return {int(number) for number in grid[row_zero_index].split(" ")}


if __name__ == '__main__':
    test = open("test_input", "r")
    lines = [line.strip() for line in test] 
    num_tests = int(lines[0])
    test_data = lines[1:]
    
    pairs = lambda l: (l[i:i + 10] for i in range(0, len(l), 10))
    test_cases = [(int(test_case[0]), test_case[1:5],
                   int(test_case[5]), test_case[6:10]) 
                  for test_case in pairs(test_data)]
    for test_num, value in enumerate(test_cases):
        first_row, first_grid, second_row, second_grid = value
        choices_1 = get_choices(first_row - 1, first_grid)
        choices_2 = get_choices(second_row -1, second_grid)
        intersection = choices_1.intersection(choices_2)
        if len(intersection) == 0:
            response = "Volunteer cheated!"
        elif len(intersection) > 1:
            response = "Bad magician!"
        else:
            response = str(intersection.pop())
        print ("Case #%d: %s" % (test_num +1, response))
