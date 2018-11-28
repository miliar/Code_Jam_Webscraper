#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""cosa"""

import string

IN_FILE = open("cj1.in", "r")
NUM_TEST = IN_FILE.readline()

#  inizio ciclo

for j in range(int(NUM_TEST)):
    FIRST_ANSWER = IN_FILE.readline()
    # print("FIRST_ANSWER", FIRST_ANSWER)
    FIRST_SET = [] 
    for i in range(4):
        line = str(IN_FILE.readline())
        line_splitted = line.split()
        FIRST_SET.append(line_splitted)
        # print(line_splitted)

    SECOND_ANSWER = IN_FILE.readline()
    # print("SECOND_ANSWER", SECOND_ANSWER)
    SECOND_SET = []
    for i in range(4):
        line = str(IN_FILE.readline())
        line_splitted = line.split()
        SECOND_SET.append(line_splitted)
        # print(line_splitted)

    res = set(FIRST_SET[int(FIRST_ANSWER) - 1]).intersection(SECOND_SET[int(SECOND_ANSWER) - 1])
    print("Case #", end="")
    print(j + 1, end="") 
    print(": ", end="")

    if len(res) == 1:
        print(", ".join(str(e) for e in res))
    if len(res) > 1:
        print("Bad magician!")
    if len(res) == 0:
        print("Volunteer cheated!") 






IN_FILE.close()
