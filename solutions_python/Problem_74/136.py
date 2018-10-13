#-------------------------------------------------------------------------------
# Name:        Google Code Jam number 1 - Bot Trust
# Purpose:
#
# Author:      Excelsior!
#
# Created:     07/05/2011
# Copyright:   (c) Excelsior! 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python


#get file
raw = open("D:\A-large.in")
inputstream = raw.readlines()
#output
output = open("D:\output3.out","w")

print("There are "+str(inputstream[0])+" test cases")




def solve(case):
    blu_fin = False
    or_fin = False
    blu_count = 0
    or_count = 0
    blu_pos = 1
    or_pos = 1
    moveorder = []
    blumov = []
    orangemov = []
    count = 0
    timer = 0
    things = case.split(" ")
    for i in range(1,len(things),2):
        if(things[i]=="O"):
            moveorder.append(1)
            orangemov.append(int(things[i+1]))
        elif(things[i] == "B"):
            moveorder.append(0)
            blumov.append(int(things[i+1]))
    if(blumov==[]):
        blu_fin = True
    if(orangemov==[]):
        or_fin = True

    while(count<len(moveorder)):
        blu_pressed = False
        timer+=1
        if(blu_fin==False):
            if(blu_pos < blumov[blu_count]):
                blu_pos+=1
            elif(blu_pos>blumov[blu_count]):
                blu_pos-=1
            elif(moveorder[count]==0 and blu_pos==blumov[blu_count]):
                count+=1
                blu_count+=1
                blu_pressed = True
        if(or_fin == False):
            if(or_pos < orangemov[or_count]):
                or_pos+=1
            elif(or_pos>orangemov[or_count]):
                or_pos-=1
            elif(moveorder[count]==1 and or_pos==orangemov[or_count] and blu_pressed == False):
                count+=1
                or_count+=1
        if(blu_count == len(blumov)):
            blu_fin = True
        if(or_count == len(orangemov)):
            or_fin = True
    return timer
outputs = []
for i in range(1,len(inputstream),1):
    outputs.append('Case #'+str(i)+': '+str(solve(inputstream[i]))+"\n")
    output.write(outputs[i-1])

print(outputs)
output.close()