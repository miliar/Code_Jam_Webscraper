import math

class pancake:
    def __init__(self,radius,height):
        self.height=height
        self.radius=radius
        self.face=radius**2 
        self.edge=2*radius*height
        
def Ans(K,pancakes):
    maxTotal=0
    radSorted=sorted(pancakes, key=lambda x:x.face) #Sort the pancakes by radius
    #We want all the options for 'largest', meaning pancake K-1 or more
    for i in range(K-1,len(radSorted)):
        bigArea=radSorted[i].face+radSorted[i].edge;
        remaining=list(radSorted[:i]) #The ones smaller than bigPancake
        edgeSorted=sorted(remaining, key=lambda x:x.edge, reverse=True) #We want the biggest edges
        edgeSum=0
        for j in range(K-1): edgeSum+=edgeSorted[j].edge
        total=edgeSum+bigArea
        if(total>maxTotal): maxTotal=total
    return math.pi * maxTotal
            
        

numCases=int(raw_input())
for case in range(numCases):
    line1Arr=raw_input().split(" ")
    N=int(line1Arr[0])
    K=int(line1Arr[1])
    pancakes=[]
    for i in range(N):
        pancakeLineArr=raw_input().split(" ")
        pancakes.append(pancake(int(pancakeLineArr[0]),int(pancakeLineArr[1])))
    print("Case #"+str(case+1)+": "+str(Ans(K,pancakes)))
    
    
