#!/usr/bin/env python


def solve(shyness):
    num_invited = 0
    num_standing = 0

    for i in range(0, len(shyness)):
        if shyness[i] == 0:
            continue
        elif i > num_standing:
            num_to_invite = (i - num_standing)
            num_invited += num_to_invite
            num_standing += num_to_invite
        num_standing += shyness[i]

    return num_invited

if __name__ == '__main__':
    #infile = 'A-tiny.in'
    infile = 'A-large.in'
    outfile = 'A-large.out'

    shyness_list = []
    with open(infile, 'r') as ifile:
        for i, line in enumerate(ifile, start=1):
            if i == 1:
                continue
            _, shyness = line.strip().split(' ')
            shyness = map(int, list(shyness))
            shyness_list.append(shyness)

    with open(outfile, 'w') as ofile:
        for i, shyness in enumerate(shyness_list, start=1):
            sol = solve(shyness)
            ofile.write('Case #%d: %d\n' % (i, sol))
