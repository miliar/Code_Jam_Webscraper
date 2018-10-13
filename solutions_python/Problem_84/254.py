#!/usr/bin/env python


def solve(mat,start):
    row = len(mat)
    column = len(mat[0])
    if start == row - 1:
        if '#' in mat[start] :
            return False
        else:
            return True
    else:
        i = 0
        while i < column:
            if mat[start][i] == '#':
                if not (mat[start][i+1] == '#' and mat[start+1][i] == '#' and mat[start+1][i+1] == '#'):
                    return False

                mat[start][i] = '/'
                mat[start][i+1] = '\\'
                mat[start+1][i] = '\\'
                mat[start+1][i+1] = '/'
                i = i+1
            i = i+1

        return solve(mat,start+1)

def show(mat):
    for i in mat:
        string = ''
        for j in i:
            string = string + j
        print string[:-1]

            

if __name__ == '__main__':
    f = open('input')
    a = int( f.readline() )
    for case in range(a):
        row , column = map (int,f.readline().split())
        matrix =[None for i in range(row)]
        for num in range(row):
            matrix[num] = list(f.readline())
        
        result = solve(matrix,0)
        print "Case #"+str(case+1)+":"
        if result == False:
            print "Impossible"
        else:
            show( matrix)
