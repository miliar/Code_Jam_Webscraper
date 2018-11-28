__author__ = 'daljeetv'
import time


f = open("inputStandingOvation.txt", 'r')
lines = f.readlines()
for idx, a in enumerate(lines):
    lines[idx] = str(lines[idx]).replace("\n", "")
    lines[idx] = lines[idx].split(" ")
    temp = []

for mm, a in enumerate(lines[1:]):
    num = str(a[1])
    count = 0
    for idx, l in enumerate(num):
        if(count >=idx):
            count+=int(l)
    num = list(num)
    num = [int(x) for x in num]
    # print count
    added = 0
    if(count < int(a[0])):
        while(count < int(a[0])):
            count = 0
            num[0]+=1
            added+=1
            for idx, l in enumerate(num):
                if(count >=idx):
                    count+=l

    print "Case #"+str(mm+1)+": " + str(added)






f.close()



