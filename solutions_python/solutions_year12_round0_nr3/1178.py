#Small
data = open('C:\CodeJam2012InOut\QualificationRound\CSI.in')
out = open('C:\CodeJam2012InOut\QualificationRound\CSO.out', 'w')
#Large
#data = open('C:\CodeJam2012InOut\QualificationRound\CLI.in')
#out = open('C:\CodeJam2012InOut\QualificationRound\CLO.out', 'w')
lines = data.readlines()
#lines = ['10','99']
#print lines
i = 1
#words = lines[1].split()

def solve(time, b):
    final = 0
    final2 = 0
    final3 = 0
    final4 = 0
    if time <= 9:
        return 0
    elif time <= 99:
        for x in range(b-time):
            if ((x+time+1)%10)*10+((x+time+1)/10) > (x+time+1) and  ((x+time+1)%10)*10+((x+time+1)/10) <= b:
                final4 = final4 + 1
                #print ((x+time+1)%10)*10+((x+time+1)/10)
                #print (x+time+1)
        return final4
    elif time <= 999:
        #$print b
        for x in range(b-time):
                a = 0
                aa = 0
                #print (x+time)
                #print '*'
                #print ((x+time)%10)*100+((x+time)/10)
                #print '***'
                #print ((x+time)%100)*10+((x+time)/100)
                #print '**********'
                if ((x+time)%10)*100+((x+time)/10) > (x+time) and ((x+time)%10)*100+((x+time)/10) <= b:
                    #print 'a'
                    #print ((x+time)%10)*100+((x+time)/10)
                    #print (x+time)
                    final = final + 1
                    a = 1
                if ((x+time)%100)*10+((x+time)/100) > (x+time) and ((x+time)%100)*10+((x+time)/100) <= b:
                    #print 'b'
                    #print ((x+time)%100)*10+((x+time)/100)
                    #print (x+time)
                    final3 = final3 + 1
                    aa = 1
                if ((x+time)%100)*10+((x+time)/100) == ((x+time)%10)*100+((x+time)/10) and (a == 1 or aa == 1):
                    final2 = final2 - 1
                    #print 'c'
                    #print (x+time)
        return final+final2+final3

for x in range(int(lines[0])):
    current = lines[x+1].split()
    anwser = solve(int(current[0]), int(current[1]))
    print "Case #%d: %s" %(x+1, anwser)

print 'out'
data.close()
out.close()
