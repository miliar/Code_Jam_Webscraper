
import sys
import string

data = sys.stdin.readlines()

nbSamples = int(data.pop(0))
print "nbSamples: ", nbSamples

def show(array, n, m):
#    for li in range(n):
#        for co in range(m):
#            print array[li, co], " ",
#        print
#    print
    return

def sub(arraya, arrayb, n, m):
    arr = {}
    for li in range(n):
        for co in range(m):
            arr[li, co] = arraya[li, co] - arrayb[li, co]
    return arr

currSample = 1

for sample in range(nbSamples):

    n, m = map(int, data.pop(0).rstrip().split())

#    print "n: ", n
#    print "m: ", m
    
    # Get the array
    array = {}

    for li in range(n):
        newline = map(int, data.pop(0).rstrip().replace(' ', ''))
        for co in range(m):
            array[li, co] = newline[co]

    # Get the actual size
    max = 0
    for li in range(n):
        for co in range(m):
            if array[li, co] > max:
                max = array[li, co]

    actual = {}
    for li in range(n):
        for co in range(m):
            actual[li, co] = max

    show(array, n, m)
    show(sub(actual, array, n, m), n, m)

    print "Case #" + str(currSample) + ":",
    currSample = currSample + 1

    isDoable = 1
    
    for li in range(n):
        for co in range(m):
            cell = array[li, co]

            # Test if for cell, either all elements of the lines are larger or equal, or the same for the column. Else, we can't do it
            isDoableForThisCell = 0
            isDoableForThisCellByLine = 1
            isDoableForThisCellByCol = 1
            
            for cocu in range(m):
                if array[li, cocu] > cell:
                    isDoableForThisCellByLine = 0
                    break
                    
            for licu in range(n):
                if array[licu, co] > cell:
                    isDoableForThisCellByCol = 0
                    break

            if isDoableForThisCellByLine == 0 and isDoableForThisCellByCol == 0:
                print "NO"
#                print "Cell ", li, co
                isDoable = 0
                break

        if isDoable == 0:
            break

    if isDoable == 0:
        continue

    print "YES"

# The algorithm:
# Cut to maximal size
# Get the current diff between actual and what you want
# If there is a 0 line / column, you don't want to do anything here
# If there is a x line / column, you can cut  x there
# If there is some >0 in a line/column where there is 0, you can't cut
# More generally: take a cell (i, j): if all values are stricly larger in the lines / columns, you can't cut -> clean lot of things there





