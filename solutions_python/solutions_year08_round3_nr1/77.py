import os
import re
os.chdir("C:\Documents and Settings\Administrator\Desktop")
print os.listdir(".")
f=open("input.txt","r")
f1=open("output.txt","w")
n=int(f.readline()[0:-1])
for i in range(0,n):
    line=f.readline()[0:-1]
    data=re.split(" ",line)
    P=int(data[0])
    K=int(data[1])
    L=int(data[2])
    line=f.readline()[0:-1]
    frequencies=re.split(" ",line)
    for j in range(0,len(frequencies[:])):
       frequencies[j]=int(frequencies[j])
    frequencies.sort()
    frequencies.reverse()
    count=0
    loop=1
    counter=0
    for j in frequencies:
        if counter < K :
            count+=loop*j
            counter+=1
        else:
            counter=0
            loop+=1
            count+=loop*j
            counter+=1
    print count        


    f1.write("Case #" + str(i+1) + ": " + str(count))
    f1.write("\n")
f.close()
f1.close()
