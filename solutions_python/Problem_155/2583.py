in1 = open ('input')
out1 = open ( 'output', 'w' )


n = int(in1.readline())
for i in range(0, n):
    str1,str2 = in1.readline().split(' ', 1)
    l = int(str1)
    m = 0
    ans = 0
    for j in range (0,l):
        m += int(str2[j]) - 1
        if m<0:
            m = 0
            ans += 1
    print "Case %d#: %d" %(i+1, ans)


in1.close();
out1.close();
