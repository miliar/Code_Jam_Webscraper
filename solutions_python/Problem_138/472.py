f = open('D-large.in', 'r')
f1 = open('workout.txt','w')
case=f.readline()
#print case
for casecount in range (0,int(case)):
    number=int(f.readline())
    used=[0]*number
    #print "case"
    #print casecount
    answer= f.readline().strip().split(' ')
    answer=map(float,answer)

    answer1= f.readline().strip().split(' ')
    answer1=map(float,answer1)
    answer.sort()
    answer1.sort()
    ##war
   # print answer
   # print answer1
    flag=1
    win=0
    for i in answer:
        index=0
        #print i,index
        for j in answer1:
            if (j>i and used[index]==0):
         #       print index,j,i
                used[index]=1
                break
            index=index+1
               

    #print len(used)-sum(used)
    war= len(used)-sum(used)
    used1=[0]*number
    used2=[0]*number
    decwar=0
    topa=0
    bota=number-1
    topb=0
    botb=number-1
    win2=0
    while (sum(used1)!=number):
        if (answer[topa]<answer1[topb]):
            used1[topa]=1
            used2[botb]=1
            topa=topa+1
            botb=botb-1
          
        else:
            used1[topa]=1
            used2[topb]=1
            topa=topa+1
            topb=topb+1
            win2=win2+1
   # print win2
    f1.write("Case #"+str(int (casecount)+1)+": "+str(win2)+" "+str(war)+"\n")
f.close()
f1.close()
        
