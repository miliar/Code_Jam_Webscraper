#problem 2 solution

def get_input():
    input_array = []
    with open("B-large.in", "r") as ins:
        cases = int(ins.readline())
        for line in ins:
            input_array.append(line)
    return input_array

def solve(problem):
    """
    solve a problem set
    """
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    problem = list(problem[:-1]) if problem[-1] == '\n' else list(problem)
    digits_left = len(problem)-1
    while(digits_left>0):
        # print problem
        if problem[digits_left]<problem[digits_left-1]:
            problem = problem[:digits_left] + ['9']*(len(problem)-digits_left)
            problem[digits_left-1] = digits[digits.index(problem[digits_left-1])-1]
        digits_left-=1
    problem = int("".join(problem))
    return problem


def solution():
    output_string = """"""
    inputs = get_input()
    for count, problem in enumerate(inputs):
        output_string+="Case #{}: {}\n".format(count+1, solve(problem))
    output_file = open('output_problem2.txt', 'w+')
    output_file.write(output_string)


if __name__ == "__main__":
    solution()