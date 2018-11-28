import sys

infile = open('A-small-attempt0.in','r')
outfile = open('A-small-attempt0.out','w')

t = int(infile.readline())
for case in range(1,t+1):
    first_selection = int(infile.readline())
    first_layout = []
    first_layout.append([int(x) for x in infile.readline().split()])
    first_layout.append([int(x) for x in infile.readline().split()])
    first_layout.append([int(x) for x in infile.readline().split()])
    first_layout.append([int(x) for x in infile.readline().split()])
    first_row = first_layout[first_selection - 1]

    second_selection = int(infile.readline())
    second_layout = []
    second_layout.append([int(x) for x in infile.readline().split()])
    second_layout.append([int(x) for x in infile.readline().split()])
    second_layout.append([int(x) for x in infile.readline().split()])
    second_layout.append([int(x) for x in infile.readline().split()])
    second_row = second_layout[second_selection - 1]

    matches = []
    for first in first_row:
        for second in second_row:
            if first == second:
                matches.append(first)

    outline = 'Case #' + str(case) + ': '
    if len(matches) == 1:
        outline += str(matches[0]) + '\n'
    elif len(matches) > 1:
        outline += 'Bad magician!' + '\n'
    else:
        outline += 'Volunteer cheated!' + '\n'
    outfile.write(outline)
