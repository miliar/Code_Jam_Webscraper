def greedy(getfarm,farmrate,maxscore):
    farmnumber=0
    totaltime=0
    if maxscore < getfarm:
        totaltime+=float(maxscore)/float(2)
        output.append(totaltime)
        return
    else:
        totaltime+=float(getfarm)/float(2)
        while True:
            time1=float(float(maxscore-getfarm)/(float(farmnumber)*float(farmrate)+2))
            time2=float(maxscore)/ float(float(farmnumber+1)*float(farmrate)+2)
            if time1 <= time2:
                totaltime+=time1
                output.append(totaltime)
                return
            else:
                farmnumber+=1
                totaltime+=float(getfarm)/float(float(farmnumber)*float(farmrate)+2)
                continue
f=open("clickin.txt")
g=open("clickout.txt","w")
testcasenum=int(f.readline().strip())
output=[]
for line in f:
    getfarm,farmrate,maxscore=[float(i) for i in line.strip().split()]
    greedy(getfarm,farmrate,maxscore)
    continue
for x in range(0,len(output)):
    g.write("Case #"+str(x+1)+": "+str(output[x])+"\n")
f.close()
g.close()
         
