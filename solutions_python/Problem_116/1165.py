#!/usr/bin/python

import re
import sys

input_file = sys.stdin


test_cases_num = int (input_file.readline ())

for i in xrange (1, test_cases_num + 1):
    lines = []
    lines.append (input_file.readline ())
    lines.append (input_file.readline ())
    lines.append (input_file.readline ())
    lines.append (input_file.readline ())
    lines.append (lines[0][0] + lines[1][0] + lines[2][0] + lines[3][0])
    lines.append (lines[0][1] + lines[1][1] + lines[2][1] + lines[3][1])
    lines.append (lines[0][2] + lines[1][2] + lines[2][2] + lines[3][2])
    lines.append (lines[0][3] + lines[1][3] + lines[2][3] + lines[3][3])
    lines.append (lines[0][0] + lines[1][1] + lines[2][2] + lines[3][3])
    lines.append (lines[0][3] + lines[1][2] + lines[2][1] + lines[3][0])

    is_cats_game = True
    ended_in_win = False

    for line in lines:
        match = re.search (r"(OOOO)|(XXXX)", line)
        if (match):
            if (match.groups ()[0]):
                print 'Case #' + str (i) + ': O won' 
            else:
                print 'Case #' + str (i) + ': X won' 
            ended_in_win = True
            break
        match = re.search (r"(^.?O.?O.?O.?$)|(^.?X.?X.?X.?$)", line)
        if (match and \
            re.search (r"T", line)):
            if (match.groups ()[0]):
                print 'Case #' + str (i) + ': O won' 
            else:
                print 'Case #' + str (i) + ': X won' 
            ended_in_win = True
            break
        if (re.search (r"\.", line)):
            is_cats_game = False

    if (not ended_in_win):
        if (is_cats_game):
            print 'Case #' + str (i) + ': Draw'
        else:
            print 'Case #' + str (i) + ': Game has not completed'
        

    input_file.readline ()

    

     
    


