from string import *
CaseNum  = input()
f = file('out.txt', 'w')
for i in range(1,CaseNum+1):
    line1 = raw_input()
    line2 = raw_input()
    line3 = raw_input()
    line4 = raw_input()
    line5 = raw_input()
    listline = [line1,line2,line3,line4]
    flag = 0 #0 draw, 1 not ,2 X, 3,O
    Dnum = 0
    #every line
    for listi in range(4):
        Xnum =0
        Onum =0
        Tnum =0
        for j in range(4):
            if listline[listi][j]=='X':
                Xnum+=1
            elif listline[listi][j]=='O':
                Onum+=1
            elif listline[listi][j]=='T':
                Tnum+=1
            elif listline[listi][j]=='.':
                Dnum+=1
        #print Xnum,Onum,Tnum
        if Xnum+Tnum==4 or Xnum==4:#X
            flag=2
            break
        if Onum+Tnum==4 or Onum==4:#O
            flag=3
            break
    #every row
    for j in range(4):
        Xnum =0
        Onum =0
        Tnum =0
        for listi in range(4):
            if listline[listi][j]=='X':
                Xnum+=1
            elif listline[listi][j]=='O':
                Onum+=1
            elif listline[listi][j]=='T':
                Tnum+=1
        #print Xnum,Onum,Tnum
        if Xnum+Tnum==4 or Xnum==4:#X
            flag=2
            break
        if Onum+Tnum==4 or Onum==4:#O
            flag=3
            break
    #cross
    Xnum =0
    Onum =0
    Tnum =0
    for listi,j in ((0,0),(1,1),(2,2),(3,3)):
        if listline[listi][j]=='X':
            Xnum+=1
        elif listline[listi][j]=='O':
            Onum+=1
        elif listline[listi][j]=='T':
            Tnum+=1
        #print Xnum,Onum,Tnum
        if Xnum+Tnum==4 or Xnum==4:#X
            flag=2
            break
        if Onum+Tnum==4 or Onum==4:#O
            flag=3
            break
    Xnum =0
    Onum =0
    Tnum =0
    for listi,j in ((0,3),(1,2),(2,1),(3,0)):
        if listline[listi][j]=='X':
            Xnum+=1
        elif listline[listi][j]=='O':
            Onum+=1
        elif listline[listi][j]=='T':
            Tnum+=1
        #print Xnum,Onum,Tnum
        if Xnum+Tnum==4 or Xnum==4:#X
            flag=2
            break
        if Onum+Tnum==4 or Onum==4:#O
            flag=3
            break
    #print "Dnum",Dnum
    output=""
    if flag==0 and Dnum>0:
        flag=1
    if flag==0:
        output="Draw"
    elif flag==1:
        output="Game has not completed"
    elif flag==2:
        output="X won"
    elif flag==3:
        output="O won"
    f.write("Case #"+str(i)+": "+output+"\n")
f.close()
