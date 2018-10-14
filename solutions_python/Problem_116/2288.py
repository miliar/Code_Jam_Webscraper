# Timothy Cohen
# 04/12/2013
# Google Code Jam Qualifying Round
#
# Tic-Tac-Toe-Tomek

import sys

def main():
    
    input_fn  = sys.argv[1]
    output_fn = input_fn.replace( 'in', 'out' )
    input_fd  = open( input_fn, 'r' )


    i               = 1
    numberTestCases = int(input_fd.readline())
    numberTestCases += 1
    testCases       = input_fd.readlines()
    lineCount       = 0


    while i < numberTestCases:
        ticTacWhoWon( i, testCases, lineCount )

        i         += 1
        # each board has 4 rows, plus 1 blank line in the file
        lineCount += 5

def ticTacWhoWon( i, testCases, lineCount ):
    
    stillPlaying = False

    row1       = testCases[lineCount].strip()
    lineCount += 1
    row2       = testCases[lineCount].strip()
    lineCount += 1
    row3       = testCases[lineCount].strip()
    lineCount += 1
    row4       = testCases[lineCount].strip()
    lineCount += 1

    column1 = row1[0] + row2[0] + row3[0] + row4[0] 
    column2 = row1[1] + row2[1] + row3[1] + row4[1] 
    column3 = row1[2] + row2[2] + row3[2] + row4[2] 
    column4 = row1[3] + row2[3] + row3[3] + row4[3] 

    diagonal1 = row1[0] + row2[1] + row3[2] + row4[3]
    diagonal2 = row1[3] + row2[2] + row3[1] + row4[0]

    possibilities = []
    possibilities.append(row1)
    possibilities.append(row2)
    possibilities.append(row3)
    possibilities.append(row4)

    possibilities.append(column1)
    possibilities.append(column2)
    possibilities.append(column3)
    possibilities.append(column4)

    possibilities.append(diagonal1)
    possibilities.append(diagonal2)
    
    for possibility in possibilities:

        if '.' in possibility:
            stillPlaying = True

        if ( possibility.count('X') == 4 ) or \
                ( possibility.count('X') == 3 and 'T' in possibility ):
            print "Case #%s: X won" % i
            return

        if ( possibility.count('O') == 4 ) or \
                ( possibility.count('O') == 3 and 'T' in possibility ):
            print "Case #%s: O won" % i
            return

    if stillPlaying:
        print "Case #%s: Game has not completed" % i
    else:
        print "Case #%s: Draw" % i 

if __name__ == "__main__":
    main()
