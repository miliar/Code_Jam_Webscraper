#!/usr/bin/python
import sys,os
from operator import itemgetter


def solve(lawn):
    """Returns a string result to one lawn of a problem
     Possible output: {"YES","NO"}"""
    # for each row find minimum
    # make sure that in mimimums column minimum is maximum
    # else fail
    for y, row in enumerate(lawn):
        minimum = min(row)
        maximum = max(row)
        min_pos_list = [i for i, j in enumerate(row) if j == minimum]
        max_pos_list = [i for i, j in enumerate(row) if j == maximum]
        for x in min_pos_list:
            height = row[x] 
            if not is_row_min_and_col_max(height,row,get_col(lawn, x)) \
            and not is_row_max_and_col_min(height,row,get_col(lawn, x)):
                return "NO"
    return "YES"

def get_row(matrix, row):
    return matrix[row]

def get_col(matrix, col):
    return [itemgetter(col)(i) for i in matrix]

def is_row_min_and_col_max(num, row, col):
    return (num == min(row)) and (num == max(col))

def is_row_max_and_col_min(num, row, col):
    return (num == max(row)) and (num == min(col))


# Shared ######################################################################
def main():
    with open(sys.argv[1], 'rU') as f_in:
        
        cases = int(f_in.readline().strip())
        for case in range(1,cases+1):
            #Get lawn dimansions
            y,x = [int(_) for _ in f_in.readline().strip().split()]
            lawn = []
            for row in range(y):
                lawn.append([int(x) for x in f_in.readline().strip().split()])
            #Solve and output
            print("Case #{}: {}".format(case, solve(lawn)))
    
if __name__ == '__main__':
    if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
        main()
    elif len(sys.argv) > 1 and not os.path.exists(sys.argv[1]):
        print "File '"+str(sys.argv[1])+"' does not exist!"
    else:
        print "No file supplied! Run program this way: '"+str(sys.argv[0])+" something.in'"
