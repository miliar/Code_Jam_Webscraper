#!/usr/bin/env python3

import sys

def main():
    output = []
    i = 1
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    for line in lines[1:]:
        a = digitize(line.strip())
        output.append('Case #{}: {}\n'.format(i, a))
        i += 1
    with open('output.txt', 'w') as f:
        for o in output:
            f.write(o)

def digitize(tc):
    A = []
    temp = tc
    zeros = temp.count('Z')
    twos = temp.count('W')
    fours = temp.count('U')
    temp = temp.replace('F', '', fours)
    fives = temp.count('F')
    temp = temp.replace('I', '', fives)
    temp = temp.replace('V', '', fives)
    sixs = temp.count('X')
    temp = temp.replace('I', '', sixs)
    sevens = temp.count('V')
    temp = temp.replace('N', '', sevens)
    eights = temp.count('G')
    temp = temp.replace('I', '', eights)
    temp = temp.replace('H', '', eights)
    nines = temp.count('I')
    temp = temp.replace('N', '', nines * 2)
    ones = temp.count('N')
    threes = temp.count('H')
    
    A.append('0' * zeros)
    A.append('1' * ones)
    A.append('2' * twos)
    A.append('3' * threes)
    A.append('4' * fours)
    A.append('5' * fives)
    A.append('6' * sixs)
    A.append('7' * sevens)
    A.append('8' * eights)
    A.append('9' * nines)
    
    return ''.join(A)

if __name__ == "__main__":
    main()
