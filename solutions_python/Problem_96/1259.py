#!/usr/bin/env python
#!/usr/bin/env python
import os
import math


#check whether the triplet is surprising or not
def isTripletSurprising((n1, n2, n3)):
    diff1 = math.fabs(n1 - n2)
    diff2 = math.fabs(n2 - n3)
    diff3 = math.fabs(n1 - n3)
    
    if ((diff1 > 2) or (diff2 > 2) or (diff3 > 2)):
        return -1
    
    if ((diff1 == 2) or (diff2 == 2) or (diff3 == 2)):
        return 1
    
    return 2


#get best non surprising triplet
def getBestTriplets(totalPoints):
    #constraints: each score: [0, 10], totalScore = totalPoints
    
    surprisingTriplets = []
    nonSurprisingTriplets = []
    
    for i in range(0, 11):
        num1 = (10 - i)
        
        for j in range(num1 - 2, num1 + 3):
            num2 = j
            
            if num2 < 11 and num2 > -1:                
                num3 = totalPoints - num1 - num2
                
                if num3 < 11 and num3 > -1 :
                    
                    flag = isTripletSurprising((num1, num2, num3))
                    
                    if(flag == 1):
                        surprisingTriplets.append((num1, num2, num3))
                    elif(flag == 2):
                        nonSurprisingTriplets.append((num1, num2, num3))
                       
    surprisingTriplet = None
    surprisingNonTriplet = None
    
    if len(surprisingTriplets) > 0:
        surprisingTriplet = surprisingTriplets[0]
        
    if len(nonSurprisingTriplets) > 0:
        surprisingNonTriplet = nonSurprisingTriplets[0]
    
    return (surprisingTriplet, surprisingNonTriplet)




#select surprising such that number of dancers >= p is maximized
def getMaxNumberOfDancers(lstTotalPoints, S, p):
    lst = []
    for totalPoints in lstTotalPoints:
        try:
            #print (getBestTriplets(totalPoints))
            lst.append(getBestTriplets(totalPoints))
        except:
            continue
        
    #lst = (sorted(lst))
    #print lst
    finalMaxNumber = 0
    count = 0
    markedIndex = set()
    
    
    #check if S satifed
    if(count < S):
    
        #iterate through list and find tuple such that non-surprising < p and susrprising >= p
        for index in range(0, len(lst)):
            
            if(count >= S):
                break
            
            surprise = None
            nonSurprise = None
            
            if(lst[index][0]):
                surprise = lst[index][0][0]
                
            if(lst[index][1]):
                nonSurprise = lst[index][1][0]
            
            if surprise >= p and nonSurprise < p and (not index in markedIndex):
                markedIndex.add(index)
                finalMaxNumber += 1
                count += 1
        
        
        
    #check for remaining items
    #iterate through list and find tuple such that non-surprising < p and susrprising >= p
    for index in range(0, len(lst)):
        
        if index in markedIndex:
            continue
        
        nonSurprise = None
        
        if(lst[index][1]):
            nonSurprise = lst[index][1][0]
            
            if(nonSurprise >= p):
                finalMaxNumber += 1 
    


    return finalMaxNumber





#select surprising such that number of dancers >= p is maximized
def getMaxNumberOfDancers1(lstTotalPoints, S, p):
    lst = []
    for totalPoints in lstTotalPoints:
        try:
            #print (getBestTriplets(totalPoints))
            lst.append(getBestTriplets(totalPoints))
        except:
            continue
        
    lst = (sorted(lst))
    print lst
    
    
    count = 0
    finalMaxNumber = 0
    #get max number of dancers
    for i in range(0, len(lst)):
        index = len(lst) - 1 - i
        
        if count < S and (lst[index][0]):
            maxNumberInCurrentTuple = lst[index][0][0]
            
            if(maxNumberInCurrentTuple >= p):
                finalMaxNumber += 1
                
                #TODO: is this correct
                count += 1
             
        #else either the surprising tuple is none or already accounted S   
        else:
            #just check is either of the tuple has a number >= p
            num1 = None
            num2 = None
            
            if(lst[index][0]):
                if count < S:
                    num1 = lst[index][0][0]
                
            if(lst[index][1]):
                num2 = lst[index][1][0]
            
            if(num1 >= p) or (num2 >= p):
                finalMaxNumber += 1


    return finalMaxNumber




#solve problem
def solveDanceProblem(N, S, p, lstTotalPoints):
    return getMaxNumberOfDancers(lstTotalPoints, S, p)




#IO
def problemIO(inputFile):
    text = open(inputFile, "rb").read()
    lines = text.split("\n")
    
    #take first line - no. of test cases
    cases = int(lines[0].strip())
    
    #DS
    outputNumbers = []
    
    
    #handle each test case
    for line in lines[1:]:
        googlerese = line.strip()
        if(googlerese):
            fields = line.split(" ")
            N = int(fields[0].strip())
            S = int(fields[1].strip())
            p = int(fields[2].strip())
            
            lstTotalPoints = []
            for i in range(0, N):
                lstTotalPoints.append(int(fields[3 + i].strip()))
        
            #solve each case
            outputNumbers.append(solveDanceProblem(N, S, p, lstTotalPoints))
        
    return outputNumbers



#output
def formatOutput(outputFile, outputNumbers):
    F = open(outputFile, "wb")
    
    for i in range(0, len(outputNumbers)):
        out = "Case #" + str(i + 1) + ": " + str(outputNumbers[i])
        print out
        F.write(out + "\r\n")
    
    
    F.close()
   
   
   
    
#unit tests
if __name__ == '__main__':
    fileLoc = "C:\\Users\\manish_ramani\\Dropbox\\projects\\google_codejam\\"
    
    #input
    outputNumbers = problemIO(fileLoc + "B-large.in")
    
    #output
    formatOutput(fileLoc + "danceOutBig.out", outputNumbers)
    
    
    #test solution
    #pts = [15, 13, 11]
    #print getMaxNumberOfDancers(pts, 1, 5)
    #print solveDanceProblem(len(pts), 2, 8, pts)




