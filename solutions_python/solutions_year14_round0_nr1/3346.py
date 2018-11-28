#!/usr/bin/python

import sys

#debug_on = True
debug_on = False

if (len(sys.argv) > 2):
    input_file = open(sys.argv[1], 'r')
    output_file = open(sys.argv[2], 'w')

else:
    print "Input and output files not specified"
    sys.exit(1)

num_cases = int(input_file.readline().strip())

def pdebug(line):
    if debug_on:
        print line

def poutput(line):
    print line
    output_file.write("%s\n" % line)

for i in (range(1, num_cases + 1)):

    first_line = []
    second_line = []

    # read the data
    first_choice = int(input_file.readline().strip())
    pdebug("First choice: %s" % first_choice)

    # advance to the selected row
    for j in range(1, first_choice):
        input_file.readline()

    first_line = [int(x) for x in input_file.readline().split(" ")]

    # skip the rest of the rows
    for j in range(first_choice, 4):
        input_file.readline()

    pdebug("First line: %s" % first_line)

    second_choice = int(input_file.readline().strip())
    pdebug("Second choice: %s" % second_choice)

    # advance to the selected row
    for j in range(1, second_choice):
        input_file.readline()

    second_line = [int(x) for x in input_file.readline().split(" ")]

    # skip the rest of the rows
    for j in range(second_choice, 4):
        input_file.readline()

    pdebug("Second line: %s" % second_line)

    matches = set(set(first_line) & set(second_line))

    if len(matches) < 1:
        result = "Volunteer cheated!"
    elif len(matches) > 1:
        result = "Bad magician!"
    elif len(matches) == 1:
        result = "%s" % matches.pop()

    else:
        print "Uh oh!"
        sys.exit(1)

    pdebug(matches)
    pdebug(len(matches))

    # print the summary line for this case
    poutput("Case #%s: %s" % (i, result))
