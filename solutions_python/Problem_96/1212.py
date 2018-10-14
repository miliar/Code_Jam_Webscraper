#! /usr/bin/env python
#coding=utf-8

filename = r"C:\Users\i035514\Desktop\Codejam\Qualification\B-large"

input=file("%s.in" % filename)
output=file("%s.ou" % filename, "w")
T=int(input.readline())



for caseNum in xrange(1,T+1):
    line = input.readline().rsplit(" ")
    N = int(line[0])
    S = int(line[1])
    P = int(line[2])

    
    result = 0
    br_s = []
    br = []
    for i in xrange(3,3+N):
        score = int(line[i])
        if score ==0:
            br_s.append(-1)
            br.append(0)
        elif score > 27:
            br_s.append(-1)
            br.append(10)    
        else:
            if score%3 == 0:
                br_s.append(score/3 +1)
                br.append(score/3)
            elif score%3==1:
                br_s.append(-1)
                br.append(score/3 +1)
            else:
                br_s.append(score/3 +2)
                br.append(score/3+1)
            
    
    for bestResult in br:
        if bestResult>=P:
            result=result+1
    i=0
    while True:
        if (i>=N or S==0):
            break;
        if(br_s[i]==P):
            result=result+1
            S=S-1
        i=i+1
    
    outstring = "Case #%d: %d\n" % (caseNum, result)
    output.writelines(outstring)

print "Done"
input.close()
output.close()

            
        
        
    
    
    