import sys
sys.stdin = open("StandingOvationIn.txt","r")
sys.stdout = open("StandingOvationOut.txt","w")
t = int(raw_input().strip())
for test in range(1,t+1):
    maxi,people = raw_input().split()
    maxi = int(maxi)
    curr = 0
    tot = 0
    for shy in range(maxi+1):
        num = int(people[shy])
        add = max(0,shy - curr)
        curr += num
        curr += add
        tot += add
    print "Case","#"+str(test)+":", tot
sys.stdout.close()
