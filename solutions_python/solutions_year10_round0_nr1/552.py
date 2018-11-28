import string
#print 'Hello World'
input = open ('A-large.in')
output = open ('A-large.out','w+')
line = input.readline()
line = string.atoi(line)
for i in range(1,line+1):
    getdata = input.readline()
    getdata = getdata.split(' ')
    N = string.atoi(getdata[0])
    K = string.atoi(getdata[1])
    if (K+1)%(2**N) == 0:
        #print (K+1)/(2**N)
        output.write("Case #%d: ON\n" %i)
    else:
        #print (K+1)%(2**N)
        output.write("Case #%d: OFF\n" %i)
input.close()
output.close()
    
    
