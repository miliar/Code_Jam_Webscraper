#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Suryakant Bharti
#
# Created:     14/04/2013
# Copyright:   (c) Suryakant Bharti 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    pass
import collections
if __name__ == '__main__':
    main()
def nroftimes(char,string):
    x=0;
    for c in string:
        if c==char:
            x=x+1
    return(x)
f1=open("A-large.in","r")
f2=open("A-large.out","w")

y2=False
nrcases=f1.readline()
#print (nrcases)
x="X"
o="O"
t="T"
dot="."
gamebord=f1.readlines()
X=": X won"
draw=": Draw"
O=": O won"
XO=": Game has not completed"

#for i in range(1,x):

  # print("Case #"+str(i))
line2=[]

allTheLists = [[] for x in range(int(nrcases))]
i=0
n=0
for j in gamebord:
 if len(j)>2:

      allTheLists[i].append(j)
      if len(allTheLists[i])>3:
        i=i+1
 else:
        continue




for i in range (0,int(nrcases)):
    y2=0
    dots=0
    diag1=allTheLists[i][0][0]+allTheLists[i][1][1]+allTheLists[i][2][2]+allTheLists[i][3][3]
    diag2=allTheLists[i][0][3]+allTheLists[i][1][2]+allTheLists[i][2][1]+allTheLists[i][3][0]
    #print(allTheLists[i])

    for j in range (0,4):
        dots=dots+nroftimes(dot,allTheLists[i][j])


        oriz=allTheLists[i][n][j]+allTheLists[i][n+1][j]+allTheLists[i][n+2][j]+allTheLists[i][n+3][j]
        if (nroftimes(x,oriz)>2 and nroftimes(t,oriz)==1) or (nroftimes(x,oriz)>3):
                print("Case #"+str(i+1)+X,file=f2)
                y2=1
                break
        if (nroftimes(o,oriz)>2 and nroftimes(t,oriz)==1) or (nroftimes(o,oriz)>3):
                print("Case #"+str(i+1)+O,file=f2)
                y2=1
                break




        if (nroftimes(x,diag1)>2 and nroftimes(t,diag1)==1) or (nroftimes(x,diag1)>3):
               print("Case #"+str(i+1)+X,file=f2)
               y2=1
               break

        if (nroftimes(o,diag1)>2 and nroftimes(t,diag1)==1) or (nroftimes(o,diag1)>3):
               print("Case #"+str(i+1)+O,file=f2)
               y2=1
               break

        if (nroftimes(x,diag2)>2 and nroftimes(t,diag2)==1) or (nroftimes(x,diag2)>3):
               print("Case #"+str(i+1)+X,file=f2)
               y2=1
               break

        if (nroftimes(o,diag2)>2 and nroftimes(t,diag2)==1) or (nroftimes(o,diag2)>3):
               print("Case #"+str(i+1)+O,file=f2)
               y2=1
               break

        if (nroftimes(x,allTheLists[i][j])>2 and nroftimes(t,allTheLists[i][j])==1) or (nroftimes(x,allTheLists[i][j])>3):
            print("Case #"+str(i+1)+X,file=f2)
            y2=1
            break
        if (nroftimes(o,allTheLists[i][j])>2 and nroftimes(t,allTheLists[i][j])==1) or (nroftimes(o,allTheLists[i][j])>3):
            print("Case #"+str(i+1)+O,file=f2)
            y2=1
            break

        print(nroftimes(dot,allTheLists[2][2]))
    if dots==0 and y2==0:
         print("Case #"+str(i+1)+draw,file=f2)
         y2=1



    if y2==0:
        print("Case #"+str(i+1)+XO,file=f2)






print(nroftimes(dot,allTheLists[2][2]))


f2.close()
f1.close()