def isTidy(number):
    digits = list(str(number))
    lastSeen = 0
    for i in range(len(digits)):
        if (int(digits[i]) < lastSeen):
            return False
        lastSeen = int(digits[i])
        
    return True

def isTidyFaster(number):
    lastSeen = number % 10
    while(number > 0):
        print ("last seen", lastSeen)
        print ("number ", number)
        if ((number % 10) > lastSeen):
            return False
        lastSeen = number % 10
        number = number // 10 
    return True


## Open the file with read only permit
f = open('input.txt', "r")
fp = open('output.txt',"w")

## use readlines to read all lines in the file
## The variable "lines" is a list containing all lines
lines = f.readlines()


for i in range(len(lines)):    
    if (i == 0):
        continue

    lastCounted = int(lines[i])
    currentNumber = 0
    print ("Last counted: ", lastCounted)

    #  IF the last number is tidy, return it
    if (isTidyFaster(lastCounted)):
        fp.write("Case #" + str(i) + ": " + str(lastCounted) + "\n")
        continue

    
    currentNumber = lastCounted
    while(not(isTidyFaster(currentNumber))):
        #print (currentNumber)
        currentNumber -= 1

    # Print results
    fp.write("Case #" + str(i) + ": " + str(currentNumber) + "\n")
    
        

## close the file after reading the lines.
f.close()
fp.close()
print ("Done ....")




    
