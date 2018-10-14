#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Sreyantha Chary
#
# Created:     13/04/2013
# Copyright:   (c) Sreyantha Chary 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from itertools import permutations

diagonals = [[0, 5, 10, 15], [3, 6, 9, 12]]
horizontals = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
verticals = [[0, 4, 8, 12], [1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15]]
alls = diagonals + horizontals + verticals

x_answers = ['xxxt',
'xxtx',
'xxxt',
'xxtx',
'xtxx',
'xtxx',
'xxxt',
'xxtx',
'xxxt',
'xxtx',
'xtxx',
'xtxx',
'xxxt',
'xxtx',
'xxxt',
'xxtx',
'xtxx',
'xtxx',
'txxx',
'txxx',
'txxx',
'txxx',
'txxx',
'txxx',
'xxxx']

y_answers = ['ooot',
'ooto',
'ooot',
'ooto',
'otoo',
'otoo',
'ooot',
'ooto',
'ooot',
'ooto',
'otoo',
'otoo',
'ooot',
'ooto',
'ooot',
'ooto',
'otoo',
'otoo',
'tooo',
'tooo',
'tooo',
'tooo',
'tooo',
'tooo',
'oooo']

answers = {}

def get(string, i):
    ret = ''
    for index in i:
        ret += string[index]
    return ret.strip()

def get_answer(string):
    if answers.has_key(string):
        return answers[string]
    else:
        dots = []
        for i in range(16):
            if string[i]=='.':
                dots.append(i)
        to_check = []
        for i in alls:
            if len(set.intersection(set(i), set(dots))) == 0:
                to_check.append(i)
        if len(to_check) == 0:
            answers[string] = 'Game has not completed'
            return answers[string]
        for i in to_check:
            test = get(string, i)
            if test.lower() in x_answers:
                answers[string] = 'X won'
                return answers[string]
            elif test.lower() in y_answers:
                answers[string] = 'O won'
                return answers[string]
        if len(dots) == 0:
            answers[string] = 'Draw'
            return answers[string]
        else:
            answers[string] = 'Game has not completed'
            return answers[string]


test_cases = int(raw_input())
for i in range(test_cases):
    line = ''
    for j in range(4):
        line += raw_input()
    try:
        raw_input()
    except:
        pass
    line = (line.replace('\n', '')).strip()
    print "Case #%s: %s" % (str(i+1), get_answer(line.lower()))
