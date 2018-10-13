import sys
import re

def main(argv):
    ifilename = argv[1]
    ofilename = argv[2]
    ifile = open(ifilename, 'r')
    ofile = open(ofilename, 'w')
    
    numlines = ifile.readline().strip()
        
    for i in range(int(numlines)):
        N = int(ifile.readline().strip())
        matrix = [0 for x in range(N)]
        for j in range(N):
            row = ifile.readline().strip()
            rightmost = -1
            for k in range(len(row)):
                if int(row[k]) is 1:
                    rightmost = k
            matrix[j] = rightmost
                
        answer = rowswaps(N, matrix)
        ofile.write("Case #"+str(i+1)+": "+str(answer)+"\n")
    
    ifile.close()
    ofile.close()
    
def rowswaps(N, matrix):
    print N
    numswaps = 0
    while (True):
        maxrow = 0
        print matrix
        for row in range(N):
            maxrow = row
            #must switch rows
            if matrix[row] > row:
                print "must switch row"+str(row)
                #if the next row can't be moved up, find the next available one and move it up one
                if matrix[row+1] > row:
                    print "can't switch with neighbor..."
                    swapped = False
                    for toswap in range(row+1, N):
                        if matrix[toswap] <= row:
                            print "    instead, switching row "+str(toswap-1)+" with row "+str(toswap)
                            tmp = matrix[toswap-1]
                            matrix[toswap-1] = matrix[toswap]
                            matrix[toswap] = tmp
                            numswaps += 1
                            swapped = True
                            break
                else:
                    print "CAN switch with neighbor"
                    tmp = matrix[row]
                    matrix[row] = matrix[row+1]
                    matrix[row+1] = tmp
                    numswaps += 1
                break

        if maxrow == N-1:
            print "maxrow: "
            print maxrow
            return numswaps
    
if __name__ == '__main__':
    main(sys.argv)