f= open('A-small-attempt3.in', 'r')
#f=open('input_ex1.txt','r')

count = 0
currentTest = 1
bSecondAnswer = False;
previousTest = 1

for line in f:

    currentTest = int((count-1)/10) + 1
    
    if (previousTest != currentTest):
        previousTest = currentTest
        bSecondAnswer = False

    realFirst  = (currentTest-1)*10 + 1
    realSecond = (currentTest-1)*10 + 6

    if count == 0:

        numTestCases = int(line)
        count += 1

    else:

        if count == realFirst:

            firstAnswer = int(line)

        elif count == realSecond:

            secondAnswer = int(line)
            bSecondAnswer = True;

        if count == (realFirst+firstAnswer):

            #print "split the 1st line"
            firstLine = line.split()
            
        elif (bSecondAnswer):

            if count == (realSecond+secondAnswer):
        
                #print "split the second line"
                secondLine = line.split()
    
        #print "lose"
        #print count 
        #print (currentTest-1)*10
        if count == (currentTest)*10:

            if (count == (realSecond + secondAnswer)) :
                secondLine = line.split()

            #print "here"
            #print count
            #print currentTest-1
            
            res = set(firstLine) & set(secondLine)

            # display final solution
            if (len(res) == 1):
                print "Case #"+str(currentTest)+": "+list(res)[0]
            elif (len(res) == 0):
                print "Case #"+str(currentTest)+": Volunteer cheated!"
            else:
                print "Case #"+str(currentTest)+": Bad magician!"
            

        count += 1

        


