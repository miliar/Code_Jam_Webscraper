#!/usr/bin/env python
# google code jam 2011
# round 1c, problem a
# Joseph Lee <GengarKhan@gmail.com>
# 5/22/11

import sys

def main(name_in, name_out):
    infile = open(name_in, 'r').read().strip().split('\n')[1:]  # input 1st arg
    if name_out != None:
        outfile = open(name_out, 'w')    # output file, 2nd cmd-line arg
    else:
        outfile=sys.stdout
    casenum=1
    while len(infile) > 0:
        R, C=infile.pop(0).strip().split(' ')    # N teams
        R=int(R)
        C=int(C)
        Ngrid=[]
        for i in range(0, R):
            Ngrid.append(CharSplit(infile.pop(0)))
        outfile.write('Case #%d:\n'%(casenum))
        fix_grid=test_case(Ngrid, R, C)
        if fix_grid==None:
            outfile.write('Impossible\n')
        else:
            for row in fix_grid:
                for ch in row:
                    outfile.write(ch)
                outfile.write('\n')
        casenum=casenum+1
    if outfile != sys.stdout:
        outfile.close()
    return 0

# main test case calculation method
def test_case(Ngrid, R, C):
    total_blue=0
    for row in Ngrid:
        total_blue+=row.count('#')
    if total_blue%4 != 0:
        return None
    #if total_blue==0:
    for r in range(0, R-1):
        for c in range(0, C-1):
            if Ngrid[r][c]=='#' and Ngrid[r][c+1]=='#' \
            and Ngrid[r+1][c]=='#' and Ngrid[r+1][c+1]=='#':
                Ngrid[r][c]='/'
                Ngrid[r][c+1]='\\'
                Ngrid[r+1][c]='\\'
                Ngrid[r+1][c+1]='/'
    total_blue=0
    for row in Ngrid:
        total_blue+=row.count('#')
    if total_blue > 0:
        return None
    return Ngrid



# parse input from command line
def parse_input(test_in):
    return None

# return list of each char in an input string
def CharSplit(string_in):
    char_ls=[]
    for i in range(0, len(string_in)):
        char_ls.append(string_in[i])
    return char_ls


if __name__=='__main__':
    name_in=sys.argv[1]
    if len(sys.argv) >= 3:
        name_out=sys.argv[2]
    else:
        name_out=None
    main(name_in, name_out)

