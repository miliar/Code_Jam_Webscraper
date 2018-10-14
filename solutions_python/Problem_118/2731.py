def C():
    #===Reading File========================================
    f = open('C-small-attempt0.in')
    T = int(f.readline())
    #=======================================================
    for t in range(T):
        A, B = f.readline().split()
        A, B = int(A), int(B)
        toBeChecked = []
        counter = 0
        #---Choosing pals to check for being square
        for i in range(A,B+1):
            if isPalindrome(str(i)):  toBeChecked.append(i)

        #---Checking to be sqaure        
        for item in toBeChecked:
            squareOf = item**0.5 
            if (squareOf)-int(squareOf)==0 and isPalindrome(str(int(squareOf))):
                counter += 1

        #---Printing the results
        print 'Case #'+str(t+1)+': '+str(counter)


#===Is Pal Function=========================================
def isPalindrome(v):
    if len(v) <= 1:
        return True
    else:
        return v[0] == v[-1] and isPalindrome(v[1:-1])
