# Solution for Google Code Jam 2012 Problem B

Bfile = open('B-large.in', 'r')
T = int(Bfile.readline())
Data = []
Data = [[int(x) for x in line.split()] for line in Bfile]
Bfile.close()
print Data

#initializing variables
c = 0 #counter for each case
i = 0 #counter for each participant within a case
regcount = 0 #count for case
speccount = 0 #count for special
special = 0 #number of specials
n = 0 #number of participants
result = [0]*T #result vector
p = 0 #minimum participant score wanted

while (c < T):
    n = len(Data[c])
    print "string length for %d is %d" %(c,n)
    special = Data[c][1]
    p = Data[c][2]
    regcount = 0
    speccount = 0
    i = 3
    while (i < n):
        if ((float(Data[c][i])/3)>(p-1)):
            regcount = regcount + 1
        elif (Data[c][i] == 0):
            speccount = speccount
        elif ((float(Data[c][i]+2)/3)>(p-1)):
            speccount = speccount + 1
        i = i + 1
    if (speccount > special):
        speccount = special
    result[c] = speccount + regcount
    c = c + 1

print result    

c = 0
RFile = open("B-large-result.txt", 'w')
while (c < T):
    RFile.write("Case #%d: %d\n" %(c+1,result[c]))
    c = c + 1

