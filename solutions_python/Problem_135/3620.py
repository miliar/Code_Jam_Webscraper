#!/usr/bin/python

import sys

if __name__ == "__main__":
    testcases = int(input())

    for case in range(1, testcases + 1):
        first_answer_row = int(input())
        
        first_rows = [[]]
        for i in range(4):
            first_rows.append(input().split())

        second_answer_row = int(input())
        second_rows = [[]]
        for i in range(4):
            second_rows.append(input().split())

        
        possible_answers = [ n for n in first_rows[first_answer_row] if n in second_rows[second_answer_row]] 

        result = ''
        if len(possible_answers) == 1:
            result = possible_answers[0]
        elif len(possible_answers) > 1:
            result = "Bad magician!"
        else:
            result = "Volunteer cheated!"

        print("Case #%d: %s" % (case, result))
        


