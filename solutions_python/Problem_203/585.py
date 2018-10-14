# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
def main():
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        R, C = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case

        elements = []

        # read in the letters
        for j in xrange(0, R):
            rowIn = raw_input()
            rowIn = list(rowIn)
            elements.append(rowIn)
        #print elements

        # for first row
        # check if first row has a letter
        colresult = checkrowforletter(elements, 0, C)
        if colresult == -1: #nothing in first row...
            #check next rows
            currColResult = -1
            currRow = 0
            while (currColResult == -1):
                currRow += 1 #update row
                currColResult = checkrowforletter(elements, currRow, C)

            #this row actually has letters
            rowWithLetters = currRow
            #copy row over to all higher rows
            for x in xrange(0, rowWithLetters):
                elements[x] = elements[rowWithLetters]
            #print elements

        #okay great, first row has letters in it
        #for each row..
        for j in xrange(0, R):
            colresult = checkrowforletter(elements, j, C) #check current row for letters
            if colresult == -1: #if nothing in row, copy upper row down
                elements[j] = elements[j - 1]
                colresult = checkrowforletter(elements, j, C) #find first occurrence of letter
            #copy first letter to all empty slots to its left
            for y in xrange(0, colresult): #y is col
                elements[j][y] = elements[j][colresult]

            #print elements
            #now go to the right of the first letter we found
            for y in xrange(colresult, C):
                #print elements
                if elements[j][y] is '?':
                    #print elements[j][y]
                    #print j
                    #print y
                    elements[j][y] = elements[j][y - 1]

        #print elements
        print "Case #{}:".format(i)
        for z in xrange(0, R):
            print "".join(elements[z])


                    #else:
            #oh we found a letter, cool

            #fill stuff to the left of letter




    # check if there is a letter in row
    # if there isn't...

    # if there is...





    #fix this later
    # check out .format's specification for more formatting options
#returns col index of first letter found
def checkrowforletter(elements, rowNum, c):
    for k in range(0, c):
        if elements[rowNum][k] != '?':
            return k
    return -1 #if not found



if __name__ == "__main__":
    main()
