with open('input0.in') as f:
    lines = f.readlines()

with open('output0.out', 'w') as output:
    N = int(lines[0])
    for c,i in enumerate(range(1,10*N,10)):
        x = map(int,lines[i+int(lines[i])].split(' '))
        y = map(int,lines[i+5+int(lines[i+5])].split(' '))
        a = [0 for j in xrange(0,17)]
        f=[0,-1]
        for j in xrange(0,4):
            a[x[j]]+=1
            a[y[j]]+=1
        for j in xrange(0,17):
        	# print a[j],
        	if a[j] == 2:
        		f[0]+=1
        		f[1]=j
        # print (f,x,y,a)
        if f[0]==1:
            output.write('Case #'+str(c+1)+': '+str(f[1])+'\n')
        elif f[0]==0:
            output.write('Case #'+str(c+1)+': '+'Volunteer cheated!'+'\n')
        else:
            output.write('Case #'+str(c+1)+': '+'Bad magician!'+'\n')
        # output.write("Case #%d: %d" % (testcase+1, alone))
