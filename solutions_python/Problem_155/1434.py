fi=open("A-large.in","r")
fo=open("A-large.out","w")
n=fi.readline()
caseNo=0
for line in fi:
        lineArray=line.strip("\n").split(" ")
        m=int(lineArray[0])
        a=lineArray[1]
        audienceTotal=0
        guestTotal=0
        for i in range(len(a)):
                shyi=int(a[i])
                guestInvited=0
                if (shyi>0) and (audienceTotal<i):
                        guestInvited=(i-audienceTotal)
                        
                audienceTotal= audienceTotal+shyi+guestInvited
                 
                 
                guestTotal=guestTotal+guestInvited
        caseNo = caseNo+1
        fo.write("Case #"+str(caseNo)+": "+str(guestTotal)+"\n")
fi.close()
fo.close()
