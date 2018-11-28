def findTidy(N):
    digits = str(N)
    prev = -1
    overIndex=-1
    over = False
    for i,d in enumerate(digits):
        if prev > d:
            over = True
            break
        else:
            if prev!=d:
                overIndex=i
            prev=d

    if over:
        ans = N[:overIndex]+str(int(N[overIndex])-1)+'9'*len(N[overIndex+1:])
        if ans[0]=='0':
            ans = ans[1:]
        return ans
    else:
        return N   

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
	print 'Case #'+str(i)+': ', findTidy(raw_input())


