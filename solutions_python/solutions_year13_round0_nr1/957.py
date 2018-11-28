'''
Created on Apr 13, 2013

@author: akshay
'''
fp = open("A-large.in","r")
list=fp.readlines()
list=[x.strip() for x in list]

T=int(list.pop(0))

cases=[]
i=0
while i<len(list):
    cases.append([list[i],list[i+1],list[i+2],list[i+3]])
    i+=5
    
#keys=cases.keys()

for i in range(len(cases)):
    case = cases[i]
    list1=[case[0][0],case[0][1],case[0][2],case[0][3]]
    list2=[case[1][0],case[1][1],case[1][2],case[1][3]]
    list3=[case[2][0],case[2][1],case[2][2],case[2][3]]
    list4=[case[3][0],case[3][1],case[3][2],case[3][3]]
    list5=[case[0][0],case[1][0],case[2][0],case[3][0]]
    list6=[case[0][1],case[1][1],case[2][1],case[3][1]]
    list7=[case[0][2],case[1][2],case[2][2],case[3][2]]
    list8=[case[0][3],case[1][3],case[2][3],case[3][3]]
    list9=[case[0][0],case[1][1],case[2][2],case[3][3]]
    list10=[case[0][3],case[1][2],case[2][1],case[3][0]]
    check=0
    countE=0
#    print list1,list5,list10
    if check==0:
        countX=0
        countO=0
        countT=0

        for j in list1:
            if j=='X':
                countX+=1
            if j=='O':
                countO+=1       
            if j=='T':
                countT+=1
            if j=='.':
                countE+=1
        
        if (countX==3 and countT==1) or (countX==4):
            print "Case #%d: X won"%(i+1)
            check+=1
        elif (countO==3 and countT==1) or (countO==4):
            print "Case #%d: O won"%(i+1)
            check+=1
    
    if check==0:
        countX=0
        countO=0
        countT=0

        for j in list2:
            if j=='X':
                countX+=1
            if j=='O':
                countO+=1       
            if j=='T':
                countT+=1
            if j=='.':
                countE+=1
        
        if (countX==3 and countT==1) or (countX==4):
            print "Case #%d: X won"%(i+1)
            check+=1
        elif (countO==3 and countT==1) or (countO==4):
            print "Case #%d: O won"%(i+1)
            check+=1
    
    if check==0:
        countX=0
        countO=0
        countT=0

        for j in list3:
            if j=='X':
                countX+=1
            if j=='O':
                countO+=1       
            if j=='T':
                countT+=1
            if j=='.':
                countE+=1
        
        if (countX==3 and countT==1) or (countX==4):
            print "Case #%d: X won"%(i+1)
            check+=1
        elif (countO==3 and countT==1) or (countO==4):
            print "Case #%d: O won"%(i+1)
            check+=1

    if check==0:
        countX=0
        countO=0
        countT=0

        for j in list4:
            if j=='X':
                countX+=1
            if j=='O':
                countO+=1       
            if j=='T':
                countT+=1
            if j=='.':
                countE+=1
        
        if (countX==3 and countT==1) or (countX==4):
            print "Case #%d: X won"%(i+1)
            check+=1
        elif (countO==3 and countT==1) or (countO==4):
            print "Case #%d: O won"%(i+1)
            check+=1

    if check==0:
        countX=0
        countO=0
        countT=0

        for j in list5:
            if j=='X':
                countX+=1
            if j=='O':
                countO+=1       
            if j=='T':
                countT+=1
            if j=='.':
                countE+=1
        
        if (countX==3 and countT==1) or (countX==4):
            print "Case #%d: X won"%(i+1)
            check+=1
        elif (countO==3 and countT==1) or (countO==4):
            print "Case #%d: O won"%(i+1)
            check+=1
            
    if check==0:
        countX=0
        countO=0
        countT=0

        for j in list6:
            if j=='X':
                countX+=1
            if j=='O':
                countO+=1       
            if j=='T':
                countT+=1
            if j=='.':
                countE+=1
        
        if (countX==3 and countT==1) or (countX==4):
            print "Case #%d: X won"%(i+1)
            check+=1
        elif (countO==3 and countT==1) or (countO==4):
            print "Case #%d: O won"%(i+1)
            check+=1
            
    if check==0:
        countX=0
        countO=0
        countT=0

        for j in list7:
            if j=='X':
                countX+=1
            if j=='O':
                countO+=1       
            if j=='T':
                countT+=1
            if j=='.':
                countE+=1
        
        if (countX==3 and countT==1) or (countX==4):
            print "Case #%d: X won"%(i+1)
            check+=1
        elif (countO==3 and countT==1) or (countO==4):
            print "Case #%d: O won"%(i+1)
            check+=1
            
    if check==0:
        countX=0
        countO=0
        countT=0

        for j in list8:
            if j=='X':
                countX+=1
            if j=='O':
                countO+=1       
            if j=='T':
                countT+=1
            if j=='.':
                countE+=1
        
        if (countX==3 and countT==1) or (countX==4):
            print "Case #%d: X won"%(i+1)
            check+=1
        elif (countO==3 and countT==1) or (countO==4):
            print "Case #%d: O won"%(i+1)
            check+=1
            
    if check==0:
        countX=0
        countO=0
        countT=0

        for j in list9:
            if j=='X':
                countX+=1
            if j=='O':
                countO+=1       
            if j=='T':
                countT+=1
            if j=='.':
                countE+=1
        
        if (countX==3 and countT==1) or (countX==4):
            print "Case #%d: X won"%(i+1)
            check+=1
        elif (countO==3 and countT==1) or (countO==4):
            print "Case #%d: O won"%(i+1)
            check+=1
            
    if check==0:
        countX=0
        countO=0
        countT=0

        for j in list10:
            if j=='X':
                countX+=1
            if j=='O':
                countO+=1       
            if j=='T':
                countT+=1
            if j=='.':
                countE+=1
                
        if (countX==3 and countT==1) or (countX==4):
            print "Case #%d: X won"%(i+1)
            check+=1
        elif (countO==3 and countT==1) or (countO==4):
            print "Case #%d: O won"%(i+1)
            check+=1
    
    if check==0 and countE==0:
        print "Case #%d: Draw"%(i+1)
    if check ==0 and countE!=0:
        print "Case #%d: Game has not completed"%(i+1)