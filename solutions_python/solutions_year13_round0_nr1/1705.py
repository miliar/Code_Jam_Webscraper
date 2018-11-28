#Filename:A.py

def checkrow(row):
    countx=0
    counto=0
    ift=False
    for i in range(0,4):
        if row[i] == 'X':
            countx+=1
        elif row[i] == 'O':
            counto+=1
        elif row[i] == 'T':
            ift=True
    if (countx == 3 and ift==True) or (countx == 4):
        return 1
    elif (counto == 3 and ift==True) or (counto == 4):
        return 2
    else:
        return 0

    
def checkcol(rows,num):
    countx=0
    counto=0
    ift=False
    for i in range(0,4):
        if rows[i][num] == 'X':
            countx+=1
        elif rows[i][num] == 'O':
            counto+=1
        elif rows[i][num] == 'T':
            ift=True
    if (countx == 3 and ift==True) or (countx == 4):
        return 1
    elif (counto == 3 and ift==True) or (counto == 4):
        return 2
    else:
        return 0

def checkdiag(rows,num):
    countx=0
    counto=0
    ift=False
    if num == 0:
        index=0
        for i in range(0,4):
            if rows[i][index] == 'X':
                index+=1
                countx+=1
            elif rows[i][index] == 'O':
                index+=1
                counto+=1
            elif rows[i][index] == 'T':
                index+=1
                ift=True
        if (countx == 3 and ift==True) or (countx == 4):
            return 1
        elif (counto == 3 and ift==True) or (counto == 4):
            return 2
        else:
            return 0

    elif num == 1:
        index=3
        for i in range(0,4):
            if rows[i][index] == 'X':
                index-=1
                countx+=1
            elif rows[i][index] == 'O':
                index-=1
                counto+=1
            elif rows[i][index] == 'T':
                index-=1
                ift=True
        if (countx == 3 and ift==True) or (countx == 4):
            return 1
        elif (counto == 3 and ift==True) or (counto == 4):
            return 2
        else:
            return 0

def hasempty(rows):
    empty=False
    for i in range(0,4):
        for j in range(0,4):
           if rows[i][j] == '.':
               empty=True
               break

    return empty




f=file('A-large.in')

testnum=f.readline()

for n in range(1,int(testnum)+1):
    rows=[]
    hasoutput=False
    for i in range(0,4):
        rows.append(f.readline())
    f.readline()
    #begin test case
    #row
    for i in range(0,4):
        if(checkrow(rows[i])==1):
            print "Case #%d: X won" %(n)
            hasoutput=True
            break
        elif(checkrow(rows[i])==2):
            print 'Case #%d: O won' %(n)
            hasoutput=True
            break
        #elif(checkrow(rows[i])==0)
    #col    
    for i in range(0,4):
        if(checkcol(rows,i)==1 and not hasoutput):
            print 'Case #%d: X won' %(n)
            hasoutput=True
            break
        elif(checkcol(rows,i)==2 and not hasoutput):
            print 'Case #%d: O won' %(n)
            hasoutput=True
            break
        #elif(checkcol(rows,i)==0)
    #diag
    for i in range(0,2):
        if(checkdiag(rows,i)==1 and not hasoutput):
            print 'Case #%d: X won' %(n)
            hasoutput=True
            break
        elif(checkdiag(rows,i)==2 and not hasoutput):
            print 'Case #%d: O won' %(n)
            hasoutput=True
            break
        #elif(checkdiag(rows,i)==0)
    if not hasoutput:
        if hasempty(rows):
            print 'Case #%d: Game has not completed' %(n)
        else:
            print 'Case #%d: Draw' %(n)



f.close()

