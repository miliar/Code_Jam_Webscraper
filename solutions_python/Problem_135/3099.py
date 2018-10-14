fil=open('A-small-attempt1.in','r')
lines=fil.readlines()

numtestcases=int(lines[0].strip())
i=1
j=1
with open('out.txt','w') as out:
    while i<=numtestcases and j < (len(lines)-9):
        casenum=i
        valrow1=lines[j]
        
        rowdct={}
        rowdct[1]=lines[j+1]
        rowdct[2]=lines[j+2]
        rowdct[3]=lines[j+3]
        rowdct[4]=lines[j+4]
        rowdct2={}
        valrow2=lines[j+5]
        
        rowdct2[1]=lines[j+6]
        rowdct2[2]=lines[j+7]
        rowdct2[3]=lines[j+8]
        rowdct2[4]=lines[j+9]
        usersrow1=rowdct[int(valrow1)].split()
        usersrow2=rowdct2[int(valrow2)].split()
        
        count=0
        val=None
        for item in usersrow1:
            if item in usersrow2:
                count+=1
                val=item
        
        if count==1:
            out.write("Case #%s: %s\n" %(casenum,val))
        elif count==0:
            out.write("Case #%s: Volunteer cheated!\n" %casenum)
        elif  count >1:
            out.write("Case #%s: Bad magician!\n" %casenum)
        j+=10
        i+=1
        
    
