#!/usr/bin/env python
# -*- coding: UTF-8 -*-


def guess():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        nb_test_case = int(lines[0])
        for counter in range(nb_test_case):
            first_answer = int(lines[1 + counter * 10])
            second_answer = int(lines[6 + counter * 10])
            first_row = lines[1 + counter * 10 + first_answer].split()
            second_row = lines[6 + counter * 10 + second_answer].split()
            list_answer = []
            for el in first_row:
                if el in second_row:
                    list_answer.append(el)
            with open('output.txt', 'a') as output:
                case = "Case #" + str(counter + 1) + ': '
                if len(list_answer) == 0:
                    ans_text = "Volunteer cheated!"
                elif len(list_answer) == 1:
                    ans_text = str(list_answer[0])
                elif len(list_answer) > 1:
                    ans_text = "Bad magician!"
                return_carriage = '\n'
                output.write(case + ans_text + return_carriage)


if __name__ == '__main__':
    guess()
