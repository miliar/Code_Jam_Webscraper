get = open('A-large.in').read()
f2 = open('A-large.out', 'wb')
print get
count=int(get.split('\n')[0])
div=1
friendnum=0
neednum=0
out=''
while count:
    G= get.split('\n')[div]
    T= int(G.split(' ')[0])
    S= G.split(' ')[1]
    for i in range(0,T+1):
        if friendnum+neednum>=i:
            friendnum+=int(S[i])
        else:
            neednum += i - friendnum - neednum;
            friendnum += int(S[i]);
    out+="Case #"+str(div)+": "+str(neednum)+'\n'
    friendnum=0
    neednum=0
    div+=1
    count-=1
f2.write(out)
