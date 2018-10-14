t = input()
i=0
while i<t:
    i+=1
    sol = ""
    ln = raw_input().split()
    n = int(ln[0])
    l = int(ln[1])
    h = int(ln[2])

    pl=raw_input().split()
    j=l
    while j<=h:
        sol = j
        for p in pl:
            p = int(p)
            if not ((p>j and p%j==0) or (p<j and j%p==0) or p==j):
                sol = 'NO'
        if sol==j:
            break

        j+=1
    


            




    print "Case #"+str(i)+":",

    print sol

    



    
    
    
