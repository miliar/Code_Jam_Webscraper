f = open('A-small-attempt5.in', 'r')

testcases = f.readline()
testcases = int(testcases)

f2 = open('output5.txt','w')
for x in range(1,testcases+1):
   
    answerone = int(f.readline())
    for line in range(1,answerone+1):
        firstline = f.readline()
    
    for junk in range(1,4-answerone+1):
        junkline = f.readline()
        
    answertwo = int(f.readline())

    for line in range(1,answertwo+1):
        secondline = f.readline()

    for junk in range(1,4-answertwo+1):
        junkline = f.readline()

    firstline = [int(k) for k in firstline.split(' ')]
    secondline = [int(k) for k in secondline.split(' ')]
    
    count = 0
 
    for xx in range(0,4):
        value1 = firstline[xx]
        for y in range(0,4):
            value2 = secondline[y]
            if value1 == value2:
                count = count+1
                savevalue = value1
            
    if x == testcases:
        if count == 1:
            #print "Case #%d: %d" % (x,savevalue)
            f2.write("Case #%d: %d" % (x,savevalue));
        if count == 0:
            #print "Case #%d: %s" % (x,"Bad magician!")
            f2.write("Case #%d: %s" % (x,"Volunteer cheated!"))
        if count>1:
            #print "Case #%d: %s" % (x,"Volunteer cheated!")    
            f2.write("Case #%d: %s" % (x,"Bad magician!"))
            
    if x<testcases:
        if count == 1:
            #print "Case #%d: %d" % (x,savevalue)
            f2.write("Case #%d: %d\n" % (x,savevalue));
        if count == 0:
            #print "Case #%d: %s" % (x,"Bad magician!")
            f2.write("Case #%d: %s\n" % (x,"Volunteer cheated!"))
        if count>1:
            #print "Case #%d: %s" % (x,"Volunteer cheated!")    
            f2.write("Case #%d: %s\n" % (x,"Bad magician!"))
        
f2.close()
f.close()