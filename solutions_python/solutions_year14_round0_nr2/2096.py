f = open('C:\\Users\\fishbeinb\\Documents\\hw6.txt', 'r')
lineArr=f.read().split('\n')
n = 0
for x in range(int(lineArr[n])):
    n = n + 1
    cc = lineArr[n].split()
    notend = True
    if float(cc[0]) > float(cc[2]):
        print "Case #"+str(x+1)+": " + str(float(cc[2])/2)
        notend = False
    count = 0
    speed = 2
    while notend:
        count = count + (float(cc[0]))/speed
        if ((float(cc[2]) - float(cc[0]))/speed) < float(cc[2])/(speed+float(cc[1])):
            print "Case #"+str(x+1)+": "+str(count + (float(cc[2]) - float(cc[0]))/speed)
            notend = False
        speed = speed + float(cc[1])
