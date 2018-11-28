__author__ = 'dnul'


def solve(line):
    maxSI=int(line.split(' ')[0])
    crowd=line.split(' ')[1]



    totalStand = 0
    needStand = 0

    for i in range(0,maxSI+1):
        if(int(crowd[i])>0 and totalStand<i):
            needStand+= (i - totalStand)
            totalStand+=(i-totalStand)

        totalStand+=int(crowd[i])

    return needStand







def main():
    file = open('A-large.in','r')
    size=file.readline()
    print size
    i=1
    for line in file.readlines():
        needStand=solve(line)
        print "case #" + str(i) + ": " +str(needStand)
        i+=1




main()



