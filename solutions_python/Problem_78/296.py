
t = input()
i=0
while i<t:
    i+=1
    sol = "Broken"

    ln = raw_input().split()
    n = int(ln[0])
    pd = int(ln[1])
    pg = int(ln[2])
    j=1
    divs = [1,2,4,5,10,20,25,50,100]
    divs.reverse()

    for d in divs:
        if pd%d==0 and 100/d <= n:
            lost = 100/d - pd/d

            for g in divs:
                if pg%g==0 and 100/g >= 100/d and pg/g >= pd/d and 100/g-pg/g >= lost:

                
                    sol = "Possible"
        


        


    print "Case #"+str(i)+":",
    print sol


    
    
    
