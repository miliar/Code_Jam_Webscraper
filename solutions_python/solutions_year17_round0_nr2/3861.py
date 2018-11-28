def last_tidy(n):
    s=str(n)
    f=True
    for i in range(0,len(s)-1):
        if s[i]>s[i+1]:
            f=False
            break
    if f:
        return n
    else:
        f=True
        for j in range(0,i):
            if s[i-j]!=s[i-j-1]:
                f=False
                break
        if f:
            t= '0' * (len(s)-1)
            re=s[0]+t
        else:
            t='0' * (len(s)-(i-j)-1)
            re=s[:i-j+1]+t
        return int(re)-1
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
 m=int(raw_input())  # read a list of integers, 2 in this case
 print "Case #{}: {}".format(i,last_tidy(m))
 # check out .format's specification for more formatting options
