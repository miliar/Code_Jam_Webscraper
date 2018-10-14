__author__ = 'Pravesh'

import sys


file = open("in.in","r")

sys.stdout = open("out","w")

def find_common(a, b):
    common = []
    for a_el in a:
        if a_el in b:
            common.append(a_el)
    return common

for i in range(int(file.readline())):
    first_answer = int(file.readline())
    first_deck = []
    for j in range(4):
        first_deck.append([x for x in file.readline().split()])

    second_answer = int(file.readline())
    second_deck = []
    for j in range(4):
        second_deck.append([x for x in file.readline().split()])

    common = find_common(first_deck[first_answer-1], second_deck[second_answer-1])

    answer = ""
    if len(common) == 1:
        answer = common[0]
    elif len(common) == 0:
        answer = "Volunteer cheated!"
    else:
        answer = "Bad magician!"
    print "Case #%d: %s" % (i+1, answer)