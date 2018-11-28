#!/usr/bin/python
import sys
f = open("A-small-attempt1.in", "r")
line = f.readline()
#print(line)
testcase = int(line)
for i in range(testcase): #i is testcase
    row1 = []
    row2 = []
    #print('NEW round'+str(i+1))
    ans1 = int(f.readline())-1
    for j in range(4): #j 4 rows
        splitline = f.readline().split(' ')
        splitline[3] = splitline[3].rstrip('\n')
        row1.append(splitline)
    ans2 = int(f.readline())-1
    for j in range(4):
        splitline = f.readline().split(' ')
        splitline[3] = splitline[3].rstrip('\n')
        row2.append(splitline)
    ans = 17
    anscount = 0
    for j in range(4):
        for k in range(4):
            if row1[ans1][j]==row2[ans2][k]:
                ans = row1[ans1][j]
                anscount+=1
                #print('MATCH '+str(ans)+' !!anscount '+str(anscount))
    if anscount==1:
        print('Case #'+str(i+1)+': '+ans)
    elif anscount>1:
        print('Case #'+str(i+1)+': '+'Bad magician!')
    else:
        print('Case #'+str(i+1)+': '+'Volunteer cheated!')
    del row1[0:len(row1)]
    del row2[0:len(row2)]
