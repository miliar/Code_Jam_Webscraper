#!/usr/bin/env python

def aver(list):
    return float(sum(list))/len(list)

if __name__ == '__main__':
    f = open('input')
    a = int( f.readline() )
    for case in range(a):
        number = int(f.readline())
        matrix =[None for i in range(number)]
        wins =[0 for i in range(number)]
        for row in range(number):
            matrix[row] = f.readline()
            for column in range(number):
                if column != row and matrix[row][column] == '1':
                    wins[row] += 1

        games = [ len([matrix[i][j] for j in range(number) if matrix[i][j] != '.']) for i in range(number)]
        
        wp = [float(wins[i])/games[i] for i in range(number)]
        
        owp = [aver([(wins[j] - int(matrix[j][i]))/(games[j] - 1.0) for j in range(number) if matrix[i][j] != '.']) for i in range(number)]

        oowp = [aver([owp[j] for j in range(number) if matrix[i][j] != '.']) for i in range(number)]
        
        rpi = [0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i] for i in range(number)]
        print "Case #"+str(case+1)+":"
        for i in range(number):
            print rpi[i]
