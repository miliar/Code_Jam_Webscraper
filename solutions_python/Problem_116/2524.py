#!/usr/bin/python

import sys


def main(argv):
    if len(argv)<1:
        sys.exit(1)
    else:
        inputfile = str(argv[0])
    
    with open(inputfile) as f:
        test_num = int(f.readline())
        test_cases = f.readlines()
        
    status = []
    for i in range(0, test_num):
        chars = []
        for k in range(0, 4):
            line = test_cases[i*5+k].strip()
            for c in line:
                chars.append(c)
        status.append(check_status(chars))
    print status
    print_status(status)

def print_status(status):
    f = open("output", 'w')
    i = 0
    for r in status:
        i += 1
        if r == 'X':
            f.write('Case #' + str(i) + ": X won\n")
        elif r == 'O':
            f.write('Case #' + str(i) + ": O won\n")
        elif r == '.':
            f.write('Case #' + str(i) + ": Game has not completed\n")
        elif r == 'D':
            f.write('Case #' + str(i) + ": Draw\n")
    f.close()
            
def check_status(chars):
    #test row
    for r in range(0, 4):
        a = test_same(chars[r*4 : r*4+4])
        if a != '#' and a != '.':
            return a         
    #test column
    for c in range(0, 4):
        a = test_same([chars[c], chars[c+4], chars[c+8], chars[c+12]])
        if a != '#' and a != '.':
            return a
    #test diangonal
    a = test_same([chars[0], chars[5], chars[10], chars[15]])
    if a != '#' and a != '.':
        return a
    a = test_same([chars[3], chars[6], chars[9], chars[12]])
    if a != '#' and a != '.':
        return a
    #test draw
    if '.' in chars:
        return '.'
    else:
        return 'D'
        
def test_same(four):
    if (four[0] != four[1]):
        if four[0] != 'T' and four[1] != 'T':
            return '#'
        elif four[2] != four[3]:
            return '#'
        elif not (four[2] == four[0] or four[2] == four[1]):
            return '#'
        else:
            return four[2]
    else:
        if four[2] == four[3]:
            if (four[2] != four[0]):
                return '#'
            else:
                return four[0]
        else:
            if four[2] != 'T' and four[3] != 'T':
                return '#'
            elif not (four[0] == four[2] or four[0] == four[3]):
                return '#'
            else:
                return four[0]

if __name__ == "__main__":
    main(sys.argv[1:])
