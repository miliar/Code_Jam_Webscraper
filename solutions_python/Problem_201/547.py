from collections import Counter as ct

def split(lst):
    y=(lst)//2
    z=(lst-1)//2
    assert abs(y-z)<=1
    assert y>=z
    assert y+z==lst-1
    return y,z
for c in range(int(raw_input())):
    n,k=map(int,raw_input().strip().split())
    stalls=ct({n:1})
    lst=0
    while k>0:
        lst=max(stalls)
        cnt=stalls[lst]
        del stalls[lst]
        k-=cnt
        l,r=split(lst)
        if l>=1:
            stalls+=ct({l:cnt})
        if r>=1:
            stalls+=ct({r:cnt})

    y,z=split(lst)
    print "Case #{}: {} {}".format(str(c+1),y,z)
