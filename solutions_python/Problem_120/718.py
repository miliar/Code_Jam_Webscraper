
infile = open('/home/suguman/Desktop/A-small-attempt0(1).in','r')
outfile = open('/home/suguman/Desktop/output1.txt','w')

x = int(infile.readline())
i=0
while i<x:
    l1 = (infile.readline()).split()
    r = int(l1[0])
    T = int(l1[1])
    n = 0
    while(T>=0):
        T = T - (2*r + 4*n + 1)
        n = n+1
    outfile.write('Case #'+str(i+1)+': ' + str(n-1)+'\n')
    i+=1


outfile.close()
infile.close() 
