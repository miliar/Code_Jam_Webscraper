#from Sets import set
import sys

def getIdealWarScore(listA, listB):
    if len(listA) < 1 or len(listB) < 1:
        return  0
    lastA, lastB, firstB = listA[-1], listB[-1], listB[0]
    naomiScore = 0
    if lastA > lastB:
        naomiScore = 1
        listASubset, listBSubset = listA[:-1], listB[1:]
        return naomiScore + getIdealWarScore(listASubset, listBSubset)
    else:
        listASubset, listBSubset = listA[:-1], listB[:-1]
        return getIdealWarScore(listASubset, listBSubset)
    

def getDeceitfulWarScore(listA, listB):
    #print "listA = " + str(listA)
    #print "listB = " + str(listB)
    if len(listA) == 1:
        if listA[0] > listB[0]:
            return 1
        else:
            return 0
    
    #now the main calculation
    firstA = listA[0]
    lenA = len(listA)
    for i in range(len(listA)):
        ind = lenA - i - 1
        if listB[ind] < listA[ind]: #Don't need to "waste" this block
            #print str(listB[ind]) + " < " + str(listA[ind])
            continue
        else:
            #print "ind=" + str(ind) + "," + str(listA[-ind]) + ", " + str(listB[-ind])
            listASubset = listA[1:]
            listBSubset = listB[0:ind] + listB[ind+1:]
            return getDeceitfulWarScore(listASubset, listBSubset)
            
    # Don't need to "waste" any of Ken's blocks - will win all the blocks
    return lenA

sys.setrecursionlimit(1500)
ifile = open("D-large.in","r")
T = ifile.next().rstrip("\n")

for i in range (int(T)):
    #print "Case #" + str(i+1)
    N = ifile.next().rstrip("\n")
    naomiRow = ifile.next().rstrip("\n").split(" ")
    kenRow = ifile.next().rstrip("\n").split(" ")

    naomiRowF = map(float, naomiRow)
    kenRowF = map(float, kenRow)
    naomiRowF.sort()
    kenRowF.sort()
    #print "naomiRow=" + str(naomiRowF)
    #print "kenRow=" + str(kenRowF)
    normalWarScore = getIdealWarScore(naomiRowF, kenRowF)
    deceitfulWarScore = getDeceitfulWarScore(naomiRowF, kenRowF)
    if deceitfulWarScore < normalWarScore:
        print str(i+1) + " - QC Error!"
    #print "normalWarScore => " + str(normalWarScore)
    #print "deceitfulWarScore => " + str(deceitfulWarScore)
    print "Case #" + str(i+1) + ": " + str(deceitfulWarScore) + " "+ str(normalWarScore) 

    
