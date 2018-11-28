#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      lihua
#
# Created:     11/04/2015
# Copyright:   (c) lihua 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

fr=open("C:/Users/lihua/Desktop/Google_Jam/2015_q1/A-large.in","r")
wr=open("C:/Users/lihua/Desktop/Google_Jam/2015_q1/A-large.out","w")

arraylines=fr.readlines()
case=int(arraylines[0])

for j in range(case):
    a=arraylines[j+1].split(' ')
    n=int(a[0])+1
    sx=list(a[1])
    s=[]
    for k in range(n):
        s.append(int(sx[k]))
    invite=0
    if n==0:
        invite=0
    else:
        sum=s[0]
        if s[0]==0:
            invite+=1
        for i in range(1,n):
            a=sum+invite
            if i>=a:
                invite+=(i-a)
            sum+=s[i]
    result="Case #"+str(j+1)+": "+str(invite)+"\n"
    wr.write(result)

fr.close()
wr.close()

