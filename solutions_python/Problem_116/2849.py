f = open ('aaa.txt')
num = f.readline()
num =int(num);
n = num
while (num!=0):
    num= num - 1;
    line1 = f.readline();
    line2 = f.readline();
    line3 = f.readline();
    line4 = f.readline();
    result = False;
    if line1[0]=='T':
        if line1[1]==line1[2] and line1[1] !='.':
            if line1[1]==line1[3]:
                result = True;
                print "Case #"+str(n-num)+": "+line1[1]+" won"
        elif line2[0] ==line3[0] and line2[0] !='.': 
            if line2[0]==line4[0]:
                result = True;
                print "Case #"+str(n-num)+": "+line2[0]+" won"
        elif line2[1] == line3[2] and line2[1] !='.':
            if line2[1]== line4[3]:
                result = True;
                print "Case #"+str(n-num)+": "+line2[1]+" won"
    elif line1[3]=='T':
        if line1[0]==line1[1] and line1[0] !='.':
            if line1[0] ==line1[2]:
                result = True;
                print "Case #"+str(n-num)+": "+line1[0]+" won"
        elif line2[3] ==line3[3] and line2[3] !='.':
            if line2[3]==line4[3]:
                result = True;
                print "Case #"+str(n-num)+": "+line2[3]+" won"
        elif line2[2] == line3[1]and line2[2] !='.':
            if line2[2]== line4[0]:
                result = True;
                print "Case #"+str(n-num)+": "+line2[2]+" won"
    else:
        if line1[0]==line1[1] and line1[0] !='.':
            if line1[0]==line1[2]:
                if line1[0]==line1[3]:
                    result = True;
                    print "Case #"+str(n-num)+": "+line1[0]+" won"
        elif line1[0]==line2[1] and line1[0] !='.':
            if line1[0]==line3[2]:
                if line1[0]==line4[3]:
                    result = True;
                    print "Case #"+str(n-num)+": "+line1[0]+" won"
        elif line1[3]==line2[2] and line1[3] !='.':
            if line1[3]==line3[1]:
                if line1[3]==line4[0]:
                    result = True;
                    print "Case #"+str(n-num)+": "+line1[3]+" won"
        elif line1[1]==line2[1] and line1[1] !='.':
            if line1[1]==line3[1]:
                if line1[1]==line4[1]:
                    result = True;
                    print "Case #"+str(n-num)+": "+line1[1]+" won"
        elif line1[2]==line2[2] and line1[2] !='.':
            if line1[2]==line3[2]:
                if line1[2]==line4[2]:
                    result = True;
                    print "Case #"+str(n-num)+": "+line1[2]+" won"

    if result==False:
        if line2[0]=='T' :
            if line2[1] ==line2[2] and line2[1]!='.':
                if line2[1] ==line2[3]:
                    result = True;
                    print "Case #"+str(n-num)+": "+line2[1]+" won"
        elif line2[3]=='T':
            if line2[2] ==line2[1] and line2[2]!='.':
                if line2[2]==line2[0]:
                    result = True;
                    print "Case #"+str(n-num)+": "+line2[2]+" won"
        else:
            if line2[0]==line2[1] and line2[0]!='.':
                if line2[0]==line2[2]:
                    if line2[0]==line2[3]:
                        result = True;
                        print "Case #"+str(n-num)+": "+line2[0]+" won"
    if result==False:
        if line3[0]=='T' :
            if line3[1] ==line3[2] and line3[1]!='.':
                if line3[1] ==line3[3]:
                    result = True;
                    print "Case #"+str(n-num)+": "+line3[1]+" won"
        elif line3[3]=='T':
            if line3[2] ==line3[1] and line3[2]!='.':
                if line3[2]==line3[0]:
                    result = True;
                    print "Case #"+str(n-num)+": "+line3[2]+" won"
        else:
            if line3[0]==line3[1] and line3[0]!='.':
                if line3[0]==line3[2]:
                    if line3[0]==line3[3]:
                        result = True;
                        print "Case #"+str(n-num)+": "+line3[0]+" won"
                        
    if result==False:
        if line4[0]=='T' :
            if line4[1] ==line4[2] and line4[1]!='.':
                if line4[1] ==line4[3]:
                    result = True;
                    print "Case #"+str(n-num)+": "+line4[1]+" won"
            elif line3[1] ==line2[2] and line3[1]!='.':
                if line3[1]==line1[3]:
                    result = True;
                    print "Case #"+str(n-num)+": "+line3[1]+" won"
            elif line3[0] ==line2[0] and line3[0]!='.':
                if line3[0]==line1[0]:
                    result = True;
                    print "Case #"+str(n-num)+": "+line3[0]+" won"
        elif line4[3]=='T':
            if line4[2] ==line4[1] and line4[2]!='.':
                if line4[2]==line4[0]:
                    result = True;
                    print "Case #"+str(n-num)+": "+line4[2]+" won"
            elif line3[2] ==line2[1] and line3[2]!='.':
                if line3[2]==line1[0]:
                    result = True;
                    print "Case #"+str(n-num)+": "+line3[2]+" won"
            elif line3[3] == line2[3] and line3[3]!='.':
                if line3[3] == line1[3]:
                    result = True;
                    print "Case #"+str(n-num)+": "+line3[3]+" won"
        else:
            if line4[0]==line4[1] and line4[0]!='.':
                if line4[0]==line4[2]:
                    if line4[0]==line4[3]:
                        result = True;
                        print "Case #"+str(n-num)+": "+line4[0]+" won"

    if result==False:
        if line1[0]==line2[0] and line1[0]!='.':
            if line1[0]==line3[0]:
                if line1[0] ==line4[0]:
                    result = True;
                    print "Case #"+str(n-num)+": "+line1[0]+" won"
        elif line1[3]==line2[3] and line1[3]!='.':
            if line1[3]==line3[3]:
                if line1[3] ==line4[3]:
                    result = True;
                    print "Case #"+str(n-num)+": "+line1[3]+" won"
                    
    if result==False:
        if not '.' in line1:
            if not '.' in line2:
                if not '.' in line4:
                    if not '.' in line3:
                        result = True;
                        print "Case #"+str(n-num)+": Draw"
                        
    if result==False:
        print "Case #"+str(n-num)+": Game has not completed"
    line = f.readline();
    

