
def solve(maxlevel, data):
    global ouf, casenum

    casenum += 1    #next case
    curpeople = int(data[0]) #init currrent people
    ans = 0
    for i in range(1, int(maxlevel) + 1):
        num = int(data[i])
        #print str(curpeople) + " " + str(num) + " i" + str(i)
        if (curpeople >= i):
            curpeople += num
        else:
            ans += (i - curpeople)
            curpeople += (i - curpeople)
            curpeople += num
            
            
    #print ("Case #" + str(casenum) + ": " + str(ans))
    ouf.write("Case #" + str(casenum) + ": " + str(ans) + "\n")
    

inf = open("A-large.in", "r")
ouf = open("out.txt", "w")
T = int(inf.readline())  #total cases
casenum = 0

for i in range(0, T):
    maxlevel, data = inf.readline().split()
    solve(maxlevel, data)

ouf.close()
