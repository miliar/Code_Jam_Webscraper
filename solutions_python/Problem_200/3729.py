import sys

n = int(input())
i = 0
while i < n:
    i += 1
    a = list(input())
    #print(a)
    l = len(a)
    last = '0'
    ii = -1
    for x in a:
        if last > x:
            break
        last = x
        ii += 1
    if ii != l-1:
        flag = 1
        while flag:
            if ii and (a[ii] == a[ii-1]):
                ii -= 1
            else:
                a[ii] = str(int(a[ii])-1)
                a[ii+1:] = ['9']*len(a[ii+1:])
                flag = 0

    print("Case #%d: %d"%(i, int(''.join(a))))
