#!/usr/bin/env python3

count = int(input())
for x in range(1,count+1):
    row_ind = int(input())
    for i in range(1,5):
        if i == row_ind:
            row_1 = input().split()
        else:
            input()
    row_ind = int(input())
    for i in range(1,5):
        if i == row_ind:
            row_2 = input().split()
        else:
            input()
    rows = row_1 + row_2
    rows.sort()
    answers = []
    for i in range(0, len(rows)-1):
        if rows[i] == rows[i+1]:
            answers.append(rows[i])
    if len(answers) == 0:
        answer = "Volunteer cheated!"
    elif len(answers) == 1:
        answer = answers[0]
    else:
        answer = "Bad magician!"

    print ("Case #" + str(x) + ": " + answer)
