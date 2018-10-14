__author__ = 'klaxon'


class Problem:
    def __init__(self, first_answer, first_square, second_answer, second_square):
        self.first_answer = first_answer
        self.first_square = list(first_square)
        self.second_answer = second_answer
        self.second_square = list(second_square)


def read_problems_from(fileName):
    f = open("input.txt", "r")
    #first line is problem count - ignore
    f.readline()

    problems = []
    line = f.readline()
    while line:
        first_answer = int(line)

        first_square = []
        for x in range(0, 4):
            square_line = f.readline()
            first_square.append([int(num) for num in square_line.split(" ", 4)])

        second_answer = int(f.readline())
        second_square = []
        for x in range(0, 4):
            square_line = f.readline()
            second_square.append([int(num) for num in square_line.split(" ", 4)])

        problems.append(Problem(first_answer, first_square, second_answer, second_square))

        line = f.readline()

    return problems


def solve(p):
    first_line = p.first_square[p.first_answer - 1]
    second_line = p.second_square[p.second_answer - 1]
    intersection = [x for x in first_line if x in second_line]

    if not intersection:
        return "Volunteer cheated!"
    elif len(intersection) == 1:
        return repr(intersection[0])
    else:
        return "Bad magician!"


problem_list = list(read_problems_from("input.txt"))

result = ""
for (index, p) in enumerate(problem_list):
    result += "Case #" + repr(index + 1) + ": " + solve(p)
    result += "\n"

result_file = open("result.txt", "w")
result_file.write(result)
