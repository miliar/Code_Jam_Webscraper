#author: Stanisław Kacprzak

sumToScores=dict()
def isSuprising(score):
    return score[2] - score[0] == 2 or score[2] - score[1] == 2 or score[1] - score[0] ==2

def allSupprising(scores):
    for score in scores:
        if not isSuprising(score):
            return False
    return True

def anySuprising(scores):
    for score in scores:
        if isSuprising(score):
            return True
    return False

def allGood(scores,p):
    for score in scores:
        if max(score) < p:
            return False
    return True

def anyGood(scores,p):
    for s in scores:
        if max(s)>=p:
            return True
    return False

def goodIsSuprising(scores,p):
    for s in scores:
        if max(s)>=p and isSuprising(s):
            return True
    return False

def initCache():
    for i in range (0,31):
        sumToScores[i]=list()        
    scores=list()
    for i in range(0,11):
        for j in range(i,i+3):
            if j > 10:
                continue
            for k in range(i,i+3):
                if k > 10:
                    continue
                score=[i,j,k]
                score.sort()
                if score not in scores:
                    scores.append(score)
    for score in scores:
        listOfScores=sumToScores[sum(score)]
        listOfScores.append(score)

initCache()   
inputFile=open('input2.txt','r')
outputFile=open('output.txt','w')
testCases=int(inputFile.readline())
for n in range(1,testCases+1):
    numbers = inputFile.readline().split(" ")
    supprisingTriplets=int(numbers[1])
    p=int(numbers[2])
    points=numbers[3:]
    ans=0
    canReplaceWithNoProblem=0
    for point in points:
        scores=sumToScores[int(point)]
        if allSupprising(scores):
            supprisingTriplets-=1
            if anyGood(scores,p):
                ans+=1
            continue
        if allGood(scores,p):
            ans+=1
            if anySuprising(scores):
                canReplaceWithNoProblem+=1
        else:
            if anyGood(scores,p):
                ans+=1
                if goodIsSuprising(scores,p):
                    supprisingTriplets-=1;
            else:
                if anySuprising(scores):
                    canReplaceWithNoProblem+=1
    if supprisingTriplets > 0:
        if canReplaceWithNoProblem - supprisingTriplets < 0:
            ans=ans-(supprisingTriplets - canReplaceWithNoProblem)
    if supprisingTriplets < 0:
        ans=ans+supprisingTriplets
    answer="Case #" + str(n)+": " + str(ans)
    print(answer)
    outputFile.write("Case #" + str(n)+": " + str(ans)+"\n")
outputFile.close()           
        
            
            
        
