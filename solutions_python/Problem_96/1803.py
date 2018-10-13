import math
f = open("google_dance.txt")

fw = open("google_dance_output.txt","w")

n = int(f.readline())

caseNum = 0
for line in f:
    caseNum +=1
    tmpline = line.replace("\n","")
    tmpInput = tmpline.split(" ")
    N = int(tmpInput[0])
    S = int(tmpInput[1])
    p = int(tmpInput[2])
    ans = 0
    for i in range(0,N):
        t = float(tmpInput[3 + i])
        maxP =  int(math.ceil(t / 3))
        #print maxP
        if maxP >= p : 
            ans += 1
        elif (maxP == p - 1) and (S > 0) and (p > 1) :
            S -= 1
            ans += 1
   
    fw.write("Case #" + str(caseNum) + ": "+ str(ans) +"\n")
            