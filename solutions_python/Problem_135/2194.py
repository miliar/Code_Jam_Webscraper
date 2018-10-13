#!/usr/bin/env python

def calculate(row1, row2):
    answer = set(row1).intersection(row2)
    if len(answer) == 0:
        return 'Volunteer cheated!'
    if len(answer) == 1:
        return answer.pop()
    else:
        return 'Bad magician!'

def main():
    input_file = open('A-small-0.in')
    output_file = open('A-small-0.out', 'w')
    cases = int(input_file.readline())
    for case in range(1, cases + 1):
        row1_index = int(input_file.readline())
        for i in range(1, 5):
            line = input_file.readline()
            if i == row1_index:
                row1 = line.split()
        row2_index = int(input_file.readline())
        for i in range(1, 5):
            line = input_file.readline()
            if i == row2_index:
                row2 = line.split()
        solution = calculate(row1, row2)
        print(solution)
	output_file.write('Case #{0}: {1}\n'.format(case, solution))
    input_file.close()
    output_file.close()

if __name__ == '__main__':
    main()
