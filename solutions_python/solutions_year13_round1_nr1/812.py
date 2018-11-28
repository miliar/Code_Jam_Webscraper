from math import sqrt

def problem(inputText):
    outPut = open("output","w")
    inputText = open(inputText)
    numOfCases =  int(inputText.readline()[:-1])

    print numOfCases
    
    setOfMatrix = []
    for case in range(numOfCases):
        #print "Case: ", case

        line = inputText.readline()[:-1].split(" ")
        r = float(line[0])
        p = float(line[1])
        
        #print (1.0/4.0) * (sqrt( 8.0*p + 4.0*r*r -4.0*r + 1 ) - 2.0*r + 1.0)
        k = int((1.0/4.0) * (sqrt( 8.0*p + 4.0*r*r -4.0*r + 1 ) - 2.0*r + 1.0))
        
        outStr = str(k)
        outPut.write("Case #"+str(case + 1)+": " + outStr + "\n")      
        

    return setOfMatrix



if __name__ == "__main__":
    a = problem("A-small-attempt0.in")
    print "DONE" 
