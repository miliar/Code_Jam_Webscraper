file = open("test.txt",'r')
testcase = int(file.readline())
for i in range(1,testcase+1) :
    num = file.readline();
    values = file.readline();
    xor=0;
    sum=0;
    min=100000000;
    for val in values.split(' '):
        
        n=int(val)
        #print "aaa"+str(n)    
        xor ^= n
        sum += n
        if(min > n):
            min=n

    if(xor != 0 ) :
        print "Case #"+str(i)+": NO"
    else:
        print "Case #"+str(i)+": "+str(sum-min)
        

