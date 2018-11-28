#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import argparse
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-in', '--input', 
        metavar='FILE', 
        action='store', 
        type=argparse.FileType('r'), 
        help='input file', 
        default=sys.stdin)
    parser.add_argument('-out', '--output', 
        metavar='FILE', 
        action='store', 
        type=argparse.FileType('w'), 
        help='output file', 
        default=sys.stdout)
    (known_args, unknown_args) = parser.parse_known_args()
    
    n = int(known_args.input.readline().rstrip('\n'))
    
    for i in xrange(n):
        s = set()
        # 1-based row number
        row_1 = int(known_args.input.readline().rstrip('\n')) - 1
        for row_number in xrange(4):
            line = known_args.input.readline().rstrip('\n')
            if row_number == row_1:
                s.update(line.split(' '))
        # 1-based row number
        row_2 = int(known_args.input.readline().rstrip('\n')) - 1
        for row_number in xrange(4):
            line = known_args.input.readline().rstrip('\n')
            if row_number == row_2:
                s.intersection_update(line.split(' '))
        # result
        known_args.output.write('Case #{0:d}: '.format(i + 1))
        if len(s) == 1:
            known_args.output.write('{0:s}\n'.format(s.pop()))
        elif len(s) > 1:
            known_args.output.write('Bad magician!\n')
        else:
            known_args.output.write('Volunteer cheated!\n')

def match_count(pattern, words):
    prog = re.compile(pattern)
    count = int()
    for word in words:
        if prog.match(word):
            count += 1
    return count

if __name__ == '__main__':
    main()
