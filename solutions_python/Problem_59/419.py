import string
#print 'Hello World'
input = open ('A-large.in')
output = open ('A-large.out','w+')
line = input.readline()
line = string.atoi(line)
for i in range(1,line+1):
    aList= []
    count = 0
    data = input.readline()
    data = data.split(' ')
    N = string.atoi(data[0])
    K = string.atoi(data[1])
#    print N
#    print K
    for j in range(1,N+1):
        temp = input.readline()
        temp = temp[0:-1]        
        while(len(temp)!=0):
            pos = temp.rfind('/')
            if temp in aList:
                temp = temp[0:pos]
            else:
                aList.append(temp)
                temp = temp[0:pos]
#    print aList
    for j in range(1,K+1):
        temp = input.readline()
        temp = temp[0:-1]
        while(len(temp)):
            pos = temp.rfind('/')
            if temp in aList:
                temp = temp[0:pos]
            else:
                count = count + 1
                aList.append(temp)
                temp = temp[0:pos]
    output.write("Case #%d: %d\n" %(i,count))
#    print count
            
input.close()
output.close()
