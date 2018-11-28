f = open('work.txt.in', 'r')
f1 = open('workout.txt','w')
case=f.readline()
for casecount in range (0,int(case)):
    #print "case"
    #print casecount
    answer= f.readline().strip().split(' ')
    answer=map(float,answer)
    count=0
    current=0
    currentrate=2
    frate=answer[1]
    x=answer[2]
    bestcountestimate=x/currentrate
    #print "bestcountestimate"
    #print bestcountestimate
    flag=1
    lasttime=0
    while(flag):
        estimate=(x/(currentrate+frate))+(answer[0]/currentrate)
        
        #print "estimate"
        #print estimate
        bestcountestimate=x/currentrate
        if(estimate<bestcountestimate):
            count=count+(answer[0]/currentrate)
            #print "count"
            #print count
            currentrate=currentrate+frate
            #print "currentrate"
            #print currentrate
        else:
            count=count+(bestcountestimate)
            flag=0
    #print count
    f1.write("Case #"+str(int (casecount)+1)+": "+str(count)+"\n")
f.close()
f1.close()
        
