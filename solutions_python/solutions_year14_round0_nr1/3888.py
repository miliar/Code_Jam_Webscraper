
import itertools
import sys
import fileinput


def solve(lines):
    first_answer = 0
    second_answer = 0
    number_of_cases = lines[0]  # Number of Test cases
    del lines[0]
    if int(number_of_cases) > 100 or int(number_of_cases) < 1:
        exit(1)
    for i in range(len(lines)):
        lines[i] = lines[i][:-1]
    for i in range(int(number_of_cases)):
        match = 0

        first_answer = lines[i*10]  # First answer


        if int(first_answer) < 1 or int(first_answer) > 4:
            exit(1)
        #A = [lines[i*5 + 1], lines[i*5 + 2], lines[i*5 + 3], lines[i*5 + 4]]
        #B = [lines[i*5 + 6], lines[i*5 + 7], lines[i*5 + 8], lines[i*5 + 9]]
        A = []
        B = []
        A.append(lines[i*10 + 1].split(' '))
        A.append(lines[i*10 + 2].split(' '))
        A.append(lines[i*10 + 3].split(' '))
        A.append(lines[i*10 + 4].split(' '))
        B.append(lines[i*10 + 6].split(' '))
        B.append(lines[i*10 + 7].split(' '))
        B.append(lines[i*10 + 8].split(' '))
        B.append(lines[i*10 + 9].split(' '))


        second_answer = lines[(i*10 + 5)]

        if len(set(list(itertools.chain(*A)))) < 16:
            exit(1)
        if int(second_answer) < 1 or int(second_answer) > 4:
            exit(1)
        if len(set(list(itertools.chain(*B)))) < 16:
            exit(1)
        for x in range(4):
            for j in range(4):

                if int(A[int(first_answer) - 1][x]) == int(B[int(second_answer)- 1][j]):

                    match += 1
                    user_selection = int(A[int(first_answer)-1][x])

        if match == 1:
            message = str(user_selection)
        elif match > 1:
            message = "Bad magician!"
        else:
            message = "Volunteer cheated!"
        print "Case #%d:" % (i+1), message


if __name__ == "__main__":
    lines = []
    for line in fileinput.input():
        lines.append(line)
    solve(lines)







