import string
#print 'Hello World'
input = open ('A-small-attempt0.in')
output = open ('A-small-attempt0.out','w+')
line = input.readline()
line = string.atoi(line)
for i in range(1,line+1):
    count = 0
    data = input.readline()
    N = string.atoi(data)
#    print N
    if N==1:
        temp = input.readline()
#        print count
    else:
        temp1 = input.readline()
        temp1 = temp1.split(' ')
#        print temp1
        XA = string.atoi(temp1[0])
        XB = string.atoi(temp1[1])
#        print XA
#        print XB
        temp2 = input.readline()
        temp2 = temp2.split(' ')
        YA = string.atoi(temp2[0])
        YB = string.atoi(temp2[1])
        if ((XA>YA and XB<YB) or (XA<YA and XB>YB)):
                count = count +1
#    print count
    output.write("Case #%d: %d\n" %(i,count))
#    print count
            
input.close()
output.close()
