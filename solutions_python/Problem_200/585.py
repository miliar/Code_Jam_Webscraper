#!/bin/python
caseCount = int(input())
for h in range(1,caseCount+1):
    # case start
    digits = [int(n) for n in input()]
    now = 0
    last = len(digits)

    while (now<last-1) and (digits[now]<=digits[now+1]):
        now+=1
    # either ready or now lt next
    if (now!=last-1):
        # lt case
        firsthigh = now+1
        while (now>0) and (digits[now]==digits[now-1]):
            now-=1
        digits[now]=digits[now]-1
        for i in range(now+1,last):
            digits[i]=9
    if(digits[0]==0):
        digits = digits[1:]
    digits = [str(n) for n in digits]
    print("Case #{}: {}".format(h,"".join(digits)))
    # case end
