from math import sqrt
nums = []
for i in range(1,32):
    nums.append(i)

filename = open("C-small-attempt1.in",'r')
s = filename.readlines()
for i in range(len(s)):
    s[i] = s[i].replace("\n","")
cases  = int(s[0])

caseN = 1

newFile = open("output.in","w")

for i in s[1:]:
    newFile.writelines("Case #%s: " %(caseN),)
    low, high = i.split()
    low = int(low)
    high = int(high)
    counter=0
    for j in range(low, high+1):
        if sqrt(j) in nums and str(j) == str(j)[::-1]:
            if str(int(sqrt(j))) == str(int(sqrt(j)))[::-1]:
                counter+=1
    newFile.writelines(str(counter))
    caseN+=1
    newFile.writelines("\n")

newFile.close()
    
