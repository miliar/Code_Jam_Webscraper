f = open("A-small.in")
num = int(f.readline())
for i4 in range (0,num):
    temp = f.readline().split()
    chain = []
    speed1 = chain.append
    speed2 = chain.index
    for i in range (0,int(temp[0])):
        speed1(False)
    for i in range (0,int(temp[1])):
        try:
            t = speed2(False)
        except:
            t = int(temp[0])-1
        for i2 in range (t,-1,-1):
            if chain[i2] is False:
                chain[i2] = True
            else:
                chain[i2] = False
    if (False in chain) is False:
        print "Case #"+str(i4+1)+": ON"
    else:
        print "Case #"+str(i4+1)+": OFF"
            
