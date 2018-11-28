# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 09:10:39 2014

@author: poonna
"""

first_answer = 2
second_answer = 3
first_arrangement = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
second_arrangement = [[1, 2, 5, 4], [3, 11, 6, 15], [9, 10, 7, 12], [13, 14, 8, 16]]

def solve(first_answer, second_answer, first_arrangement, second_arrangement):
    first_set = set(first_arrangement[first_answer-1])
    second_set = set(second_arrangement[second_answer-1])
    answer = list(set.intersection(first_set, second_set))
    if len(answer) == 1:
        return answer[0]
    elif len(answer) == 0:
        return "Volunteer cheated!"
    else:
        return "Bad magician!"

num_tests = int(raw_input())
for i in range(num_tests):
    first_answer = int(raw_input())
    first_arrangement = []
    for j in range(4):
        line = raw_input()
        first_arrangement.append(map(int, line.split()))
    second_answer = int(raw_input())
    second_arrangement = []
    for j in range(4):
        line = raw_input()
        second_arrangement.append(map(int, line.split()))
    print 'Case #' + str(i+1) + ': ' + str(solve(first_answer, second_answer, first_arrangement, second_arrangement))
