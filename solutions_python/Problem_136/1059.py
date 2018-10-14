import sys

cases = int(raw_input())
words = []
for i in range(cases):
    words.append(raw_input().split(' '))

for i in range(cases):
    r = 2
    c = float(words[i][0])
    f = float(words[i][1])
    x = float(words[i][2])
    t = x/r+1
    n=0
    
    while True:
        t_old = t
        t = 0
        #print n
        for j in range(n):
            #print str(c/(r+i*f)) + " farm " + str(i)
            t += c/(r+j*f)
        #print str(x/(r+n*f)) + " objective"
        t += x/(r+n*f)

        if t > t_old:
            break;
        #print "here"
        n+=1
    t = 0
    n-=1
    for j in range(n):
        #print str(c/(r+i*f)) + " farm " + str(i)
        t += c/(r+j*f)
    #print str(x/(r+n*f)) + " objective"
    t += x/(r+n*f)
    print "Case #" + str(i+1) + ": " + str(t)
