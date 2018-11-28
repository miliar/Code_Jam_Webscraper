#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Ammar
#
# Created:     12/04/2014
# Copyright:   (c) Ammar 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    with open("inp.txt") as f:
        buff=f.readlines()
    cases=int(buff[0])
    lis=[]
    f=open("Out.txt","w")
    for i in range(0,cases,1):

        st=i*10+1
##        print st
        r=int(buff[st])
        line=buff[st+r]
        row=line.split()
##        print row
        st+=5
##        print st
        r=int(buff[st])
        line=buff[st+r]
        row2=line.split()

##        print row2
        boolean=0
        card=-1
        for rw in row:
            if rw in row2:
                boolean+=1
                card=rw
        if boolean==0:
            msg= "Case #"+str(i+1)+": "+"Volunteer cheated!"
        elif boolean==1:
            msg= "Case #"+str(i+1)+": "+str(card)
        else:
            msg= "Case #"+str(i+1)+": "+"Bad magician!"


        f.write(msg+"\n");

if __name__ == '__main__':
    main()
