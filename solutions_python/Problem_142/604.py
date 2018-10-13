import math

def read_words(afile):
    words = []
    for line in afile:
            words.append(line.strip())
    return words



filename = open('Tim.txt' , 'r')
T = filename.readline() #num test cases
aList = read_words(filename) # array where each element is a line of text

for i in range(int(T)):
    line1 = aList[1 + 3*i]
    
    line2 = aList[2 + 3*i] 
    
    array1 = []
    count1 = []
    for l in range(len(line1)-1):
        if ( line1[l] != line1[l+1] ):
            array1.append(line1[l])
    array1.append(line1[-1])

    line1 += "*"
    j = 0
    while (j < (len(line1)-1)):
        count = 1
        current = line1[j]
        while ( line1[j+1] == line1[j] ):
            count += 1
            j += 1
        count1.append(count)
        j += 1
    
    array2 = []
    count2 = []
    for l in range(len(line2)-1):
        if ( line2[l] != line2[l+1] ):
            array2.append(line2[l])
    array2.append(line2[-1])
    
    line2 += "*"
    j=0    
    while (j < len(line2)-1):
        count = 1
        current = line2[j]
        while ( line2[j+1] == line2[j] ):
            count += 1
            j += 1
        count2.append(count)
        j+=1
    
    good = True
    if (len(array1) != len(array2) ):
        good = False
    else:
        for l in range(len(array1)):
            if (array1[l] != array2[l]):
                good = False
    if (good == False):    
        print "Case #" + str(i+1) + ": Fegla Won"
    else:
        count = 0
        for x in range(len(count1)):
            count += abs(count1[x] - count2[x])
        
        print "Case #" + str(i+1) + ": " + str(count)
