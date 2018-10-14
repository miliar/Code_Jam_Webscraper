#!/usr/bin/python

import sys
from pprint import pprint
from collections import deque

TAB = '   '


def checkOppos(oppos, seq, debug = False):
    if len(seq) < 2:
        return seq
    for a in range(0, len(seq)):
        for b in range(a+1, len(seq)):
            pattern = seq[a] + seq[b]
            if pattern in oppos or pattern[::-1] in oppos:
                seq = ''
                if debug:
                    print TAB*2, pattern, 'oppos found -> [empty]'
                return seq
    return seq
    

def checkCombo(combo, seq, debug = False):
    if len(seq) < 2:
        return seq
    pattern = seq[-2:]  # last two elements
    if pattern in combo or pattern[::-1] in combo:
        try:
            seq = seq[:-2] + combo[pattern]
        except:
            seq = seq[:-2] + combo[pattern[::-1]]
        if debug:
            print TAB*2, 'combo found ->', seq
        # No recursion necessary because only non-base element is substituted
        # seq = checkCombo(combo, seq, debug)   # recurse
    return seq
    

def solveCase(combo, oppos, seq, debug = False):
    if debug:
        print 'Solving sequence: ',;   pprint(seq)
    if len(seq) < 2:
        return seq
    seq2 = str()
    for i in range(0, len(seq)):
        seq2 += seq[i]
        if debug:
            print TAB, seq2
        seq2 = checkCombo(combo, seq2, debug)
        seq2 = checkOppos(oppos, seq2, debug)
    return seq2


def main(debug = False):
    if len(sys.argv) < 2:
        print 'no input file given!'
        return
    
    fin = open(sys.argv[1])
    T = fin.readline() 
    T = int(T)

    result = list()

    for c in range(1, T+1):
        case = fin.readline().split()
        if debug:
            print case
        idx = 0
        # load combos
        combo = dict()
        C = int(case[idx]);         idx += 1
        comb = case[idx : idx+C];   idx += C
        for i in range(0, C):
            combo[ comb[i][0:2] ] = comb[i][2]
        if debug:
            print C, 'combo =', combo
        # load opposites
        oppos = list()
        D = int(case[idx]);         idx += 1
        opp = case[idx : idx+D];    idx += D
        for i in range(0, D):
            oppos.append( opp[i][0:2] )
        if debug:
            print D, 'oppos =', oppos
        # load invoke sequence
        N = int(case[idx]);         idx += 1
        seq = str( case[idx] );
        if debug:
            print N, 'seq =', seq
        magic = solveCase(combo, oppos, seq, debug = False)
        result.append(magic)
        print seq, '->', magic

    fin.close()
    writeOutput(result)
                
                
def formatMagic(result):
    magic = '['
    for i in range(0, len(result)):
        magic += result[i]
        if i != len(result)-1:
            magic += ', '
    magic += ']'
    return magic


def writeOutput(result):
    fout = open('magick.out', 'w')
    for c in range(0, len(result)):
        magic = formatMagic(result[c])
        line = 'Case #%d: %s' % (c+1, magic)
        print line
        fout.write(line)
        fout.write('\n')
    fout.close()

if __name__ == '__main__':
    debug = False
    main(debug)
    
