t = input()
for p in range(t):
    s = input()
    n = map(float,raw_input().split())
    k = map(float,raw_input().split())

    n.sort()
    k.sort()
    dw = 0
    w = 0
    i = 0
    j = 0
    while i<s and j<s:
        if n[i]>k[j]:
            dw+=1
            i+=1
            j+=1
        else:
            i+=1
    i = 0
    j = 0
    while(i<s and j<s):
        if n[i]<k[j]:
            w+=1
            i+=1
            j+=1
        else:
            j+=1
    print "Case #"+str(p+1)+":",dw,s-w
