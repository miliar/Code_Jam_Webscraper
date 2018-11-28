for n in range(int(raw_input())):
    m = raw_input().split(" ")
    r = [int(m[0])]
    for i in range(int(m[1])):
        r.sort(reverse=True)
        k = r.pop(0)
        r.append(int(k/2))
        r.append(int((k-1)/2))

    A = r.pop()
    B = r.pop()
    print "Case #"+ str(n+1)+ ": "+str(B)+" "+str(A)
