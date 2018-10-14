#!/usr/bin/python

input='A-large.in'

lines=[]
with open(input) as file:
    for line in file:
      lines.append(line.strip())

cases=lines[0]

lines = iter(lines)
next(lines)
case=0
for line in lines:
    case += 1
    maxlevel,people=line.split(' ')
    shyness=0
    standup=0
    audience=0
    need=0
    #5 110011
    #L 012345
    #S 1222
    
    #5 210011
    #L 012345
    #S 2333
    
    last_has_standup=False
        
    clapers=[]
    i=0
    need=0
    for members in people.strip():
        
        if (i == 0): standup+=int(members) # shyness = 0, stand up all members
        elif (int(members)!=0 and sum(clapers)>=shyness): standup+=int(members) # At least one stand up now, members stand up
        
        newmember=0
        miss = (shyness - sum(clapers))
        #print "members",members,"shyness",shyness,"standup",standup,"sum(clapers)",sum(clapers),"miss",miss
        if (miss>0):
            need+=1
            newmember += 1
        
        clapers.append(int(members)+newmember)
        shyness+=1
        i+=1
        audience+=int(members)
        
        
        #5 210011:1
        #L 012345
        #S 2333
        
        #stay=audience-standup
        #if (stay>0):
            #need+=(shyness-sum(clapers)) # Simulate one more stand up
            #ns+=1
        
    #seated=audience-standup
    #print "standup",standup
    #print "audience",audience
    #print "seated",seated
    #if (seated>0):
        #print "seated so need"
        #need+=1
    
    #seated=audience-standup
    #print "seated",seated
    
    print "Case #"+str(case)+": "+str(need)
    #break
 
#print cases
#print max