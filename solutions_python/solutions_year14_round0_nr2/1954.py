#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import argparse
import re
import string
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
        args = known_args.input.readline().rstrip('\n').split()
        C = float(args[0])
        F = float(args[1])
        X = float(args[2])
        
        t = float()
        j = int()
        while X/(2+j*F) > C/(2+j*F)+X/(2+(j+1)*F):
            t += C/(2+j*F)
            j += 1
        t += X/(2+j*F)
        known_args.output.write('Case #{0:d}: {1:.7f}\n'.format(i + 1, t))

if __name__ == '__main__':
    main()
