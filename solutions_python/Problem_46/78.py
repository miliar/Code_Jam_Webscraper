#!/usr/bin/env python 
################################################################################


import sys
import os
import logging

#if (os.environ.get("DEBUG") != None):
#logging.basicConfig(level=logging.DEBUG)

def main():
    input = sys.stdin
    
    # T specifies the number of test cases
    T = int(input.readline())
    logging.info("T = %d", T)
    
    for i in range(T):
        N = int(input.readline())
        matrix = []
        for n in range(N):
            matrix.append(map(str, input.readline().split()))
        processTestCase(i + 1, N, matrix)



def processTestCase(index, N, matrix):
    logging.info("index=%s, N=%s, matrix=%s" % (index, N, matrix))

    swaps = [0]

    def swaprows(i, j):
        assert abs(i - j) == 1
        if (j < i): return swaprows(j, i)
        logging.info("swaprows(%d, %d) %s %s" % (i, j, matrix[i], matrix[j]))
        swaps[0] += 1
        t = matrix[i]
        matrix[i] = matrix[j]
        matrix[j] = t
        #print matrix[i], i
        #print matrix[j], j
        #assert(matrix[i][1] <= i)
        #assert(matrix[j][1] <= j)

    def swapallrows(i, j):
        if (j < i): return swapallrows(i, j)
        logging.info("swapallrows(%d, %d) %s %s" % (i, j, matrix[i], matrix[j]))
        for x in range(j, i, -1):
            swaprows(x, x-1)

    def findpartner(row):
        for i in range(row+1, N):
            if (matrix[i][1] <= row): break
        return i
        

    def done():
        for (r, row) in enumerate(matrix):
            if (r < row[1]): return False
        return True
        

    for (r, row) in enumerate(matrix):
        # this is the min row that this matrix can be in
        row.append(row[0].rfind("1"))

    for (r, row) in enumerate(matrix):
        if (row[1] < r):
            logging.info("%s %s" %(row, "UP"))
        elif (row[1] > r):
            logging.info("%s %s" %(row, "DOWN"))
        else:
            logging.info("%s %s" %(row, ""))

    #swaprows(0, 1)

    while (not done()):
        for (r, row) in enumerate(matrix):
            if (row[1] > r):
                partner = findpartner(r)
                swapallrows(r, partner)
                break
        #         print
        #         for row in matrix:
        #             print row
        #         print

    logging.info("Case #" + str(index) + ": " + str(swaps[0]))
    print "Case #" + str(index) + ": " + str(swaps[0])
    
main()
sys.exit(0)
