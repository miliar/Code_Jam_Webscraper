import time
import math

t = time.clock()
f = open("ProblemA-Small.txt")
f.readline()

outFile = open("ProblemA-Out.txt",'w')
c = 0
vowels = ['a','e','i','o','u']
while True:
    c+=1
    data= f.readline()
    if len(data) == 0:
        break
    s = data.split(" ")
    w = s[0]
    n = int(s[1])
    con = 0
    for i in range(len(w)):
        b = 0
        for j in range(i,len(w)):
            if not w[j] in vowels:
                b+=1
                if b >= n:
                    con += len(w)-(j)
                    break
            else:
                b = 0
    message = "{0}".format(con)
    outFile.write("Case #{0}: {1}\n".format(c, message))
    print "Case #{0}: {1}".format(c, message)
    
print time.clock() - t
f.close()
outFile.close()
