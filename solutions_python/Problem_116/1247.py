t=input()
for i in range(t):
    win=0
    s1=[x for x in raw_input()]
    s2=[x for x in raw_input()]
    s3=[x for x in raw_input()]
    s4=[x for x in raw_input()]
    s5=raw_input()
    d1=[s1[0],s2[1],s3[2],s4[3]]
    d2=[s1[3],s2[2],s3[1],s4[0]]
    c1=[s1[0],s2[0],s3[0],s4[0]]
    c2=[s1[1],s2[1],s3[1],s4[1]]
    c3=[s1[2],s2[2],s3[2],s4[2]]
    c4=[s1[3],s2[3],s3[3],s4[3]]
    if (s1.count('X')+s1.count('T'))==4:
        win=1
    elif (s1.count('O')+s1.count('T'))==4:
        win=2
    elif (s2.count('X')+s2.count('T'))==4:
        win=1
    elif (s2.count('O')+s2.count('T'))==4:
        win=2
    elif (s3.count('X')+s3.count('T'))==4:
        win=1
    elif (s3.count('O')+s3.count('T'))==4:
        win=2
    elif (s4.count('X')+s4.count('T'))==4:
        win=1
    elif (s4.count('O')+s4.count('T'))==4:
        win=2
    elif (d1.count('X')+d1.count('T'))==4:
        win=1
    elif (d1.count('O')+d1.count('T'))==4:
        win=2    
    elif (d2.count('X')+d2.count('T'))==4:
        win=1
    elif (d2.count('O')+d2.count('T'))==4:
        win=2
    elif (c1.count('X')+c1.count('T'))==4:
        win=1
    elif (c1.count('O')+c1.count('T'))==4:
        win=2
    elif (c2.count('X')+c2.count('T'))==4:
        win=1
    elif (c2.count('O')+c2.count('T'))==4:
        win=2
    elif (c3.count('X')+c3.count('T'))==4:
        win=1
    elif (c3.count('O')+c3.count('T'))==4:
        win=2
    elif (c4.count('X')+c4.count('T'))==4:
        win=1
    elif (c4.count('O')+c4.count('T'))==4:
        win=2
    if win==0:
        if s1.count('.')+s2.count('.')+s3.count('.')+s4.count('.')>0:
           print "Case #"+str(i+1)+": Game has not completed" 
        else:
            #dw
            print "Case #"+str(i+1)+": Draw"
    if win==1:
        #X
        print "Case #"+str(i+1)+": X won"
    elif win==2:
        #O
        print "Case #"+str(i+1)+": O won"
