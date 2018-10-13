def decideIfCalcBroken(n,pd,pg):
    for i in range(1,n+1):
        for j in range (0,i+1):
            #print "Tried "+str(j)+" wins out of "+str(i)+" gives: "+str((float(j)/float(i))*100)
            if (float(j)/float(i) * 100== pd and pg >= j):
                if (pg==100 and j-i==0 or pg<100):
                    return True
    return False

def readInputFile(filename):
    fh=open(filename,'r')
    num_tests=int(fh.readline())
    for i in range(num_tests):
        line_nums=fh.readline()
        nums_list=line_nums.rsplit()
        n=int(nums_list[0])
        #print nums_list[0]
        pd=int(nums_list[1])
        #print nums_list[1]
        pg=int(nums_list[2])
        #print nums_list[2]
        if(decideIfCalcBroken(n,pd,pg)):
            print "Case #"+str(i+1)+": Possible"
        else:
            print "Case #"+str(i+1)+": Broken"
