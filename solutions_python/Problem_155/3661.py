case = int(raw_input())
for iterator in range(0,case):
    temp = raw_input()
    temp = temp.split(" ")
    Smax = int(temp[0])
    queue = temp[1]
    standing = 0
    invited = 0
    for i in range(0,Smax+1):
        if(standing >= i):
            standing = standing + int(queue[i])
        else:
            if(int(queue[i]) != 0):
                invited = invited + (i - standing)
                standing = standing + invited + int(queue[i])
    print "Case #"+str(iterator+1)+": "+str(invited)
