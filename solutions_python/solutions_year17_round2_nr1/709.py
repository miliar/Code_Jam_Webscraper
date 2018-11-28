import logging
import numpy as np
import random

def horse(filename='inputA.in'):
    #reader
    rownum = 0
    numbers = list()
    j = 0
    with open('Input/' + filename, 'rb') as file:
        f = open('Output/' + filename.split('.')[0] + '.out', 'w')
        for row in file:
            # print(row)
            if rownum > 0:
                j += 1
                row = row.split()
                D = int(row[0])
                N = int(row[1])
                print('D: ' + str(D))
                print('N: ' + str(N))
                minD = 0
                for i in range(N):
                    nrow = next(file)
                    nrow = nrow.split()
                    K = int(nrow[0])
                    S = int(nrow[1])
                    loopD = (D-K)/S
                    minD = max(minD, loopD)
                f.write('Case #' + str(j) + ': ' + str(D/minD) + '\n')
                    # print('inner: ' + str(nrow))
                    
                # numbers.append(int(row.rsplit))
            rownum += 1
    # logging.debug('List of numbers: ' + str(numbers))
    
    # #writer
    # with open('Output/' + filename.split('.')[0] + '.out', 'w') as file:
    #     for i in range(len(solList)):
    #         file.write('Case #' + str(i+1) + ': ' + solList[i] + '\n')


if __name__ == "__main__":

    FORMAT = '%(levelname)s: %(message)s'
    logging.basicConfig(format=FORMAT, level=logging.DEBUG)

    horse('inputA.in')












