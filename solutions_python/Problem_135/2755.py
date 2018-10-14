#!/usr/bin/python

num_cases = int(raw_input())
for case_no in range(1, num_cases+1):
    first_row   = int(raw_input()) - 1
    first_board = []
    for i in range(4):
        line = raw_input()
        first_board.append(map(int,line.split(' ')))
    second_row   = int(raw_input()) - 1
    second_board = []
    for i in range(4):
        line = raw_input()
        second_board.append(map(int,line.split(' ')))
    possible_nums = list(set(first_board[first_row]).intersection(set(second_board[second_row])))
    print "Case #%d:" % case_no,
    if len(possible_nums) == 1:
        print possible_nums[0]
    elif len(possible_nums) == 0:
        print "Volunteer cheated!"
    else:
        print "Bad magician!"

