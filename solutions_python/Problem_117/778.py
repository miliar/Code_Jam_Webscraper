#!/usr/bin/env python
# Google Code Jam Qualification Round
# Lawnmower Problem
# Author: Nick Mooney

from sys import argv, exit

def is_possible(number, row, column):
    if max(row) > number and max(column) > number:
        return False
    return True

def check_matrix(lawn, height, width):
    """Takes a list of lists, height, width"""
    for i in range(height):
        for j in range(width):
            if not is_possible(lawn[i][j], lawn[i], [lawn[x][j] for x in range(height)]):
                return False
    return True

def process_file(lines):
    num_rounds = int(lines[0])
    del(lines[0])
    
    for round in range(num_rounds):
        height, width = [int(x) for x in lines[0].split()]
        del(lines[0])
        
        lawn = list()
        
        for i in range(height):
            lawn.append([int(x) for x in lines[0].split()])
            del(lines[0])
        
        if check_matrix(lawn, height, width):
            print("Case #%d: YES" % (round + 1))
        else:
            print("Case #%d: NO" % (round + 1))

if __name__ == "__main__":
    try:
        infile_name = argv[1]
    except:
        print("Usage: lawnmower.py <infile>")
        exit()
    
    inlines = open(infile_name,'r').read().splitlines()    
    process_file(inlines)
    
    