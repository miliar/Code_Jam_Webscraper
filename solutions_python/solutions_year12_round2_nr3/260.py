from itertools import combinations
f=open('C-small-attempt0.in','r')
outputfile=open('out','w')
numberOfEntries=float(f.readline())
#=================
counter=0
while(counter<numberOfEntries):
    counter+=1
    outputfile.write("Case #"+str(counter)+":\n")

    competitorsJudges=[]
    line=f.readline()
    line=line.split()
    numberOfNumbers=float(line[0])
    innerCounter=0
    total=0
    numbers=[]
    while(innerCounter<numberOfNumbers):
        innerCounter+=1
        numbers.append(int(line[innerCounter]))
    innerCounter=0
    lists=[]
    while innerCounter<numberOfNumbers:
        innerCounter+=1
        LIST=list(combinations(numbers, innerCounter))
        lists.extend(LIST)
    sums=[]
    found=False
    for innerList in lists:
            sumOfList=0
            for number in innerList:
                sumOfList+=number
            try :
                indexx=sums.index(sumOfList)
                for a in innerList:
                    outputfile.write(str(a)+ ' ')
                outputfile.write("\n")
                for a in lists[indexx]:
                    outputfile.write(str(a)+ ' ')
                outputfile.write("\n")
                found=True
                break
    
            except ValueError:
                    sums.append(sumOfList)
    if(found==False):
        outputfile.write("Impossible \n")

        
        