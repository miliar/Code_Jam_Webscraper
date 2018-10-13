def calculate(case):
        case=(str(int(case)))
        caseLength = len(case)
        if caseLength==1:
                return case
        else:
                arrayCase=[]
                for s in case:
                        arrayCase.append(int(s))
                i=0
                while i<caseLength-1:
                        if arrayCase[i]>arrayCase[i+1]:
                                arrayCase[i]=arrayCase[i]-1
                                if i>0:
                                        j=i
                                        while j!=0:
                                                if arrayCase[j]<arrayCase[j-1]:
                                                        arrayCase[j]=9
                                                        arrayCase[j-1]-=1
                                                        j-=1
                                                else:
                                                        j=0
                                k=i+1
                                while k<caseLength:
                                        arrayCase[k]=9
                                        k+=1
                                return answer(arrayCase)
                        i+=1       
                return answer(arrayCase)

def answer(numList):         
    s = map(str, numList)   # ['1','2','3']
    s = ''.join(s)          # '123'
    s = int(s)              # 123
    return s                        
j=0
f = open('C:/Users/Vedat/Desktop/VAK/Coding/Python/Codejam 8.4.17/B-large.in','r')
numberOfCases=f.readline()
numberOfCases = int(numberOfCases)
while j<numberOfCases:
    case=f.readline()
    print('Case #'+str(j+1)+': '+ str(calculate (case)))
    j+=1
