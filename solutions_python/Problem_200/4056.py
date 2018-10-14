f1=open('input.txt','r+')
f2=open('output.txt','w+')
for t in xrange(int(f1.readline())):
    num = int(f1.readline())
    tidy = 0
    for i in xrange(num,-1,-1):
        s = str(i)
        flag = 1
        for j in xrange(0,len(s)-1):
            if s[j]>s[j+1]:
                flag = 0
                break
        if flag:
            tidy = i
            break
    f2.write("Case #{}: {}\n".format(t+1, tidy))
f1.close()
f2.close()
