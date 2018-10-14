import math
import random


def finalCheck(positions,students):
    for circle1 in range(0,len(positions)-1):
        for circle2 in range(circle1+1,len(positions)):
            curDistance=distance(positions[circle1],positions[circle2])
            sumRadii=students[circle1]+students[circle2]
            if sumRadii>curDistance:
                return False
    return True

def distance(point1,point2):
    curX=(point1[0]-point2[0])**2
    curY=(point1[1]-point2[1])**2
    return math.sqrt(curX+curY)

def circlesIntersect(positions,students,newPosition,currentStudent):
    for circle1 in range(0,len(positions)):
        curDistance=distance(positions[circle1],newPosition)
        sumRadii=students[circle1]+currentStudent
        if sumRadii>curDistance:
            return True
    return False
            
            

def positionStudents(width,length,students):
    while True:
        testPositions=[[0,0]]
        for student in range(1,len(students)):
            counter=0
            while counter<100:
                counter+=1
                curX=random.random()*width
                curY=random.random()*length
                nextPosition=[curX,curY]
                if not circlesIntersect(testPositions,students,nextPosition,students[student]):
                    testPositions.append([curX,curY])
                    break
            else:
                break
        if len(testPositions)==len(students):
            break
            
    assert finalCheck(testPositions,students)
    answer=""
    for each in testPositions:
        answer=answer+" ".join(map(str,each))+" "
    
    return answer.rstrip().lstrip()
    
    
    

X=open("bsm3.in")
z=open("output.txt","w")
case=0
currentline=X.readline()
currentline=X.readline().rstrip().lstrip().split()
while currentline:
    case+=1
    print case
    matWidth=int(currentline[1])
    matLength=int(currentline[2])
    students=map(int,X.readline().rstrip().lstrip().split())
    z.write("Case #"+str(case)+": "+positionStudents(matWidth,matLength,students)+"\n")
    currentline=X.readline().rstrip().lstrip().split()
z.close()
