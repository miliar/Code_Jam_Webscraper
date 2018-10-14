def putans(start,end): #return string to write in file
    count=0
    for x in xrange(start,end+1):
        if x <= 10:
            continue
        elif x in [11,22,33,44,55,66,77,88,99,111,222,333,444,555,666,777,888,999,1000]:
            continue
        if x<100:
            zFlag=False
            y=x
        #flip it once
            temp = (y%10)*10
            if temp is 0:
                zFlag=True
            y=y/10
            temp = temp+(y%10)
            if temp<=end and temp>=start and temp>x and temp is not x and zFlag is False:
                count=count+1
                print x,temp
            continue



        zFlag=False
        y=x
        #flip it once
        temp = (y%10)*100
        if temp is 0:
            zFlag=True
        y=y/10
        temp = temp+(y%10)
        y=y/10
        temp = temp+(y%10)*10
        if temp<=end and temp>=start and temp>x and temp is not x and zFlag is False:
            count=count+1
            print x,temp


        zFlag=False
        y=temp
        #flip it once again
        temp = (y%10)*100
        if temp is 0:
            zFlag=True
        y=y/10
        temp = temp+(y%10)
        y=y/10
        temp = temp+(y%10)*10
        if temp<=end and temp>=start and temp>x and temp is not x and zFlag is False:
            print '2nd: ',x,temp
            count=count+1        
    return str(count)+'\n'

def main():
    f = open('small.txt','r')
    fout = open('out.txt','w')
    iter = int(f.readline())
    for i in xrange(iter):
        inp = f.readline()
        temp=inp.strip().split(' ')
        fout.write('Case #'+str(i+1)+': ')
        fout.write(putans(int(temp[0]),int(temp[1])))

if __name__ == "__main__":
    main()
