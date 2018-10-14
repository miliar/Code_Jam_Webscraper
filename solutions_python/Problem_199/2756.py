#!/usr/bin/python3
#encoding=UTF-8
def readCase():
    T=int(input())
    caseMatrix=[]
    while T>0:
        case=[]
        line=input()
        line=line.split(' ')
        #print(line[1])
        case.append(int(line[1]))
        for i in line[0]:
            if i=='+':
                case.append(1)
            else:
                case.append(-1)
        T-=1
        caseMatrix.append(case)
    #print(caseMatrix)
    return caseMatrix
def flipperPancake(caseMatrix):
    answers=[]
    
    for i in range(0,len(caseMatrix)):
        answer=''
        count=0
        K=caseMatrix[i][0]
        caseInfo=caseMatrix[i][1:]
        j=0
        while j+K<=len(caseInfo):
            tmpcount=0
            if caseInfo[j]==1:
                j+=1
            else:
                #flipperCountOfKPre+=1
                count+=1
                j0=j
                for l in range(j0,j0+K):
                    caseInfo[l]*=-1
                for l in range(j0,j0+K):
                    if caseInfo[l]==-1:
                        j=l
                        break
                    else:
                        tmpcount+=1
                if tmpcount==j0+K-1:
                    j=tmpcount
        flag=0
        for item in caseInfo[j:]:
            if item==-1:
                flag+=1
        if flag>0:
            answer='Case #'+str(i+1)+': '+'IMPOSSIBLE'+'\n'
        else:
            answer='Case #'+str(i+1)+': '+str(count)+'\n'
        answers.append(answer)
    return answers
def outPrint(answers):
    for i in answers:
        print(i)        
if __name__=='__main__':
    cases=readCase()
    answer=flipperPancake(cases)
    outPrint(answer)
