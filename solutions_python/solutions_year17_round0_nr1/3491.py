f1=open('input.txt','r+')
f2=open('output.txt','w+')
for t in xrange(int(f1.readline())):
    line=f1.readline().split()
    s=list(line[0])
    k=int(line[1])
    flip = 0
    flag = 1
    for i in xrange(len(s)-k+1):
        if s[i]=='-':
            flip+=1
            for j in xrange(i,i+k):
                if s[j]=='-':
                    s[j] = '+'
                else:
                    s[j] = '-'
    for i in xrange(len(s)-k,len(s)):
        if s[i]=='-':
            flag = 0
            break
    if flag:
        f2.write("Case #{}: {}\n".format(t+1, flip))
    else:
        f2.write("Case #{}: {}\n".format(t+1, 'IMPOSSIBLE'))
f1.close()
f2.close()
