b= open('B-large.in')
c = open('b_out.txt', 'w')
num = int(b.readline())
count=1
while count <=num:
    line=b.readline().strip()
    maxnum= int(line)
    lmax=list(line)
    if len(lmax) <2:
        c.write('Case #'+str(count)+": " +str(int(''.join(lmax))))
        c.write('\n')
    if len(lmax)==2:
        if int(lmax[0]) > int(lmax[1]) :
            lmax[0]=str(int(lmax[0])-1)
            lmax[1]=str(9)
        c.write('Case #' + str(count) + ": "+ str(int(''.join(lmax))))
        c.write('\n')
    if len(lmax)>2:
        for i in range(len(lmax)-1, 0,-1):
            if int(lmax[i])<=0:
                lmax[i] = str(9)
                for x in range(len(lmax)-1,i-1,-1):
                    lmax[x]=str(9)
                lmax[i-1]= str(int(lmax[i-1])-1)
            if int(lmax[i])<int(lmax[i-1]):
                lmax[i] = str(9)
                lmax[i-1] = str(int(lmax[i-1])-1)
                for x in range(len(lmax)-1,i-1,-1):
                    lmax[x]=str(9)
        c.write('Case #' + str(count) + ": "+str(int(''.join(lmax))))
        c.write('\n')
    count+=1