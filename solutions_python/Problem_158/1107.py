testfile=open('D-small-attempt1.in','r')
text=testfile.readlines()
ndata=[]
for i in range(1,len(text)):
    ndata.append(text[i].replace('\n',''))
    ndata[i-1]=ndata[i-1].split()
    for k in range(len(ndata[i-1])):
        ndata[i-1][k]=int(ndata[i-1][k])
for i in range(len(ndata)):
    if ndata[i][0]==1:
        won='GABRIEL'
    elif ndata[i][0]==2:
        if ((ndata[i][1]*ndata[i][2])%ndata[i][0])==0:
            won='GABRIEL'
        else:
            won='RICHARD'
    elif ndata[i][0]==3:
        if ((ndata[i][1]==3 and ndata[i][2]==3) or (ndata[i][1]==4 and ndata[i][2]==3) or (ndata[i][1]==3 and ndata[i][2]==4) or (ndata[i][1]==3 and ndata[i][2]==2) or (ndata[i][1]==2 and ndata[i][2]==3)):
           won='GABRIEL'
        else:
           won='RICHARD'
    elif ndata[i][0]==4:
        if ((ndata[i][1]==4 and ndata[i][2]==3) or (ndata[i][1]==3 and ndata[i][2]==4) or (ndata[i][1]==4 and ndata[i][2]==4)):
            won='GABRIEL'
        else:
            won='RICHARD'
    print "Case #{}:".format(i+1),won
testfile.close()   
