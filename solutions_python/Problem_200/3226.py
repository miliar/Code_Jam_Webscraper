#!/usr/bin/python

def last_tidy(num):
    ds=list(str(num)[::-1])
    i=0
    n=len(ds)
    last = int(ds[i])
    i += 1
    while i < n:
        curr = int(ds[i])
        if curr > last:
            for j in range(0,i):
                ds[j]='9'
            ds[i]=str(curr - 1)
        last = int(ds[i])
        i += 1

    return int(''.join(ds)[::-1])



nt=int(raw_input())
for i in range(nt):
    num=int(raw_input())
    ans=last_tidy(num)
    print("Case #{}: {}".format(i+1, ans))
