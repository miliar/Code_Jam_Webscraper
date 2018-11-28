f=open('A-large.in','r')
fo=open('output.txt','w')
t=int(f.readline())
for j in xrange(t):
    data = f.readline()
    data = data.split()
    ans = 0
    stoodup = int(data[1][0])
    for i in xrange(1, len(data[1])):
        if stoodup<i:
            ans+=i-stoodup
            stoodup = i
        stoodup+=int(data[1][i])
    fo.write('Case #'+str(j+1)+': '+str(ans)+'\n')
f.close()
fo.close()
