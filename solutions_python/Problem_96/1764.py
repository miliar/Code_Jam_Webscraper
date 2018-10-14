def findScores(total):
    """Finds the scores with greatest spread without being surprising from a total"""
    score1 = total/3
    score2 = (total-score1)/2
    score3 = total-(score1+score2)
    return [score1, score2, score3]

##
##def spreadScores(scores):
##    """When surprising, creates the greatest spread of scores"""
##    scores.sort()
##    if scores[1] == scores[2]:
##        scores[1] -= 1
##        scores[2] += 1
##    return scores

def Solve(TotalsList, S, p):
    """Finds the greatest number of scorers who could have had a best"""
    """score of p or more when S people were surprising."""
    ListOScores = []
    #print "-----------------------------------------"
    ListOfTotalsInt = map(int, TotalsList)
    #print len(ListOfTotalsInt)
    ListOTotals = filter(lambda x: x >=3*p-4 and x >= p, ListOfTotalsInt)
    #print p, filter(lambda x: not x in ListOTotals, ListOfTotalsInt)
    for t in ListOTotals:
        ListOScores+= [findScores(t)]
    SurpriseList = filter(lambda x: max(x) < p, ListOScores)
    OKscores = len(ListOScores)-len(SurpriseList)
    NotSurpriseList = filter(lambda x: not x in SurpriseList, ListOScores)
    #print p, " ///", SurpriseList, " ///", NotSurpriseList
    return OKscores + min(S,len(SurpriseList))
    
    
def TSolve(TotalsList, S, p):
    """Finds the greatest number of scorers who could have had a best"""
    """score of p or more when S people were surprising."""
    ListOScores = []
    ListOfTotalsInt = map(int, TotalsList)
    ListOTotals = filter(lambda x: x >=3*p-4 and x >= p, ListOfTotalsInt)
    return len(ListOfTotalsInt) - len(ListOTotals)




#The following reads in input
fileName = raw_input("Please enter the filename of input ")
f = open(fileName, 'r+')
######

#And this generates output and writes to file
T = int(f.readline())

output = ""
for n in range(1,T+1):
    line = f.readline()
    line = str.split(line)
    N = line.pop(0)
    S = int(line.pop(0))
    p = int(line.pop(0))
    output+="Case #" + str(n) + ": " + str(Solve(line, S, p)) + "\n"
print output
f.close()

g = open(fileName[:fileName.index('.')]+"_output"+
         fileName[fileName.index('.'):], "r+")
g.write(output)
