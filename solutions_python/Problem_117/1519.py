'''
Created on Apr 12, 2013

@author: hou
'''

import sys


def read_lawn(infile):
    [row, col] = [int(elem) for elem in infile.readline().split()]
    lawn = [[0] * col for i in xrange(row)]  # 2-d array to represent a lawn
    
    for i in xrange(row):
        line = infile.readline().split()
        for j, height in enumerate(line):
            lawn[i][j] = int(height)

    return lawn


def check_row(lawn, row):
    for cell in lawn[row]:
        if cell != 1: return False    
    return True


def check_col(lawn, col):
    for i in xrange(len(lawn)):
        if lawn[i][col] != 1: return False
    return True


def check_lawn(lawn):
    for i, row in enumerate(lawn):
        for j, col in enumerate(row):
            # if cell is 2, go to next cell
            if col == 2: continue
            
            # if cell is 1, check it row first
            # if it passes row check, skip to next row 
            if check_row(lawn, i): 
                break
            else:
                # check its column, if it fails, return false
                if not check_col(lawn, j):
                    return False    
    return True


def main():    

    infile = open(sys.argv[1])          # input file as the first arg
    outfile = open(sys.argv[2], 'w')    # output file as the second arg
    
    # get the number of test cases
    test_num = int(infile.readline())
        
    # for each test case, determine the status
    for i in xrange(test_num):
        lawn = read_lawn(infile)
        status = 'NO'
        if check_lawn(lawn): status = 'YES'
        outfile.write("Case #" + str(i+1) + ": " + status + '\n')
    
    # close files
    infile.close()
    outfile.close()  



if __name__=='__main__':
    main()
