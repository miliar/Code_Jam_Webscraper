#!/usr/bin/env python2.7
#
# GoogleCodeJam 2014
# Qualification Round
# A - Magic Trick
#
# Edward Lau
# eplau[at]ucla[dot]edu
# 2014.04.12






######################
## IMPORT LIBRARIES ##
######################
import sys





##############
## FILENAME ##
##############
debug = True; # true == extra info output
debug = False;
input_file = sys.argv[1];

try:
    f_handle = open(input_file, 'r');
except:
    print "Does that file exist?"
    raise





#############
## N Cases ##
#############
n_cases = int(f_handle.readline().strip());

for i_case in range(0, n_cases):
    # Read first row
    row1 = int(f_handle.readline().strip());
    if debug:
        print "Row1: {}".format(row1);

    # Skip (row1-1) lines
    for i_skip in range(0, row1-1):
        row_junk = f_handle.readline().strip();
    if debug:
        print "Skipping: {}".format(row1-1);

    # Read first possibles
    possibles1 = set();
    for i in f_handle.readline().strip().split():
        possibles1.add(int(i))
    if debug:
        print "Possibles1:"
        print possibles1

    # Skip remaining lines
    for i_skip in range(0, 4-row1):
        row_junk = f_handle.readline().strip();
    if debug:
        print "Skipping: {}".format(4-row1);



    # Read second row
    row2 = int(f_handle.readline().strip());
    if debug:
        print "Row2: {}".format(row2);

    # Skip (row1-1) lines
    for i_skip in range(0, row2-1):
        row_junk = f_handle.readline().strip();
    if debug:
        print "Skipping: {}".format(row2-1);

    # Read second possibles
    possibles2 = set();
    for i in f_handle.readline().strip().split():
        possibles2.add(int(i))
    if debug:
        print "Possibles2:"
        print possibles2

    # Skip remaining lines
    for i_skip in range(0, 4-row2):
        row_junk = f_handle.readline().strip();
    if debug:
        print "Skipping: {}".format(4-row2);



    # Find solution
    solution = possibles2.intersection(possibles1);

    if len(solution) == 0:
        case_message = "Volunteer cheated!";

    elif len(solution) == 1:
        case_message = solution.pop();

    else:
        case_message = "Bad magician!";



    # Print output
    print "Case #{}: {}".format(i_case+1, case_message);





# Close out
f_handle.close();
