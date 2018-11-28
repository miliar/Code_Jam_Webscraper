'''
Created on Apr 8, 2017

@author: jessicazhang
'''
import re

text_file = open("input", "r")
your_list = text_file.readlines()

testCases=int(your_list[0])

for i in range(1,testCases+1):
    tidy=False
    current=your_list[i].strip()
    while tidy==False:
        digits=len(current)
        if len(current)==1:
            tidy=True
            break
        count=0
        for j in range(len(current)):
            if j!=0 and int(current[j])<int(current[j-1]):
                if int(current[j])==0 and int(current[0])==1:
                    current="9"*(len(current)-1)
                    tidy=True
                    break
                else:
                    current=current[:j-1]+str(int(current[j-1])-1)+"9"*len(current[j:])
        for j in range(len(current)):
            if j!=0 and int(current[j])>=int(current[j-1]):
                count+=1
        if count==len(current)-1:
            tidy=True
            break
    print "Case #"+str(i)+": "+str(current)