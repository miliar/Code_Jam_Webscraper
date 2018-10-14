#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
import codecs

WIDTH = 4
EMPTY = '.'
PLAYER_A = 'O'
PLAYER_B = 'X'
WILDCARD = 'T'

def solve(b):
    if len(b) != 16:
        return 'Error'
    result = ''
    
    lines = [
             b[0:4], b[4:8], b[8:12], b[12:16],
             b[0]+b[4]+b[8]+b[12], b[1]+b[5]+b[9]+b[13], b[2]+b[6]+b[10]+b[14], b[3]+b[5]+b[9]+b[15],
             b[0]+b[5]+b[10]+b[15], b[12]+b[9]+b[6]+b[3]]
    
    draw = True
    for line in lines:
        if line.count(PLAYER_A) + line.count(WILDCARD) == 4:
            result = '%s won' % PLAYER_A
            draw = False
            break
        elif line.count(PLAYER_B) + line.count(WILDCARD)  == 4:
            result = '%s won' % PLAYER_B
            draw = False
            break
    if draw:
        if b.count(EMPTY) > 0:
            result = 'Game has not completed'
        else:
            result = 'Draw'
    return result

def load_file(filepath, out):
    with codecs.open(filepath, "r", "utf-8-sig") as inf:
        T = int(inf.readline().strip())
        round = 1
        board = ''
        for line in iter(inf.readline, ''):
            value = line.strip()
            if value != '':
                board += value
            else:
                result = 'Case #%d: %s\n' % (round, solve(board))
                out.write(result)
                sys.stdout.write(result)
                board = ''
                round += 1

def main():
    filepath = 'A-small-attempt1'
    outfile = open('%s.out' % filepath, 'w')
    load_file('%s.in' % filepath, outfile)
    outfile.close()

if __name__ == '__main__':
    main()