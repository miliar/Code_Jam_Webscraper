
def last_tidy(n):
    if len(n) == 1:
        return int(n)
    if len(n) == 2:
        if n[1]<n[0]:
            return str(int(n[0])-1)+'9'
    ori = n
    n = list(n)
    for i in xrange(len(n)):
        n[i]=int(n[i])
    for i in xrange(1,len(n)):
        if n[i]>=n[i-1]:
            continue
        for j in xrange(i,0,-1):
            if n[j-1]>n[j]:
                x=n[j-1]-1
                n[j-1]=x
                digit=j-1
#        print x, digit
        if digit == 0:
            if x==0:
                return '9'*(len(n)-1)
            else:
                return str(x)+'9'*(len(n)-1)
        ans=''
        for k in xrange(digit):
            ans+=str(n[k])
        ans+=str(x)
        for k in xrange(len(n)-len(ans)):
            ans+='9'
        return ans
    return ori

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n = raw_input()  # read a list of integers, 2 in this case
    print "Case #{}: {}".format(i, last_tidy(n))
    # check out .format's specification for more formatting options
    