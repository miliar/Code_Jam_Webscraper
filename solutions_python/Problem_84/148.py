t = input()
i=0
while i<t:
    i+=1
    sol = ""
    ln = raw_input().split()
    r = int(ln[0])
    c = int(ln[1])
    j = 0
    rs = []
    while j<r:
        j+=1
        sor = []
        for ch in raw_input():
            sor += [ch]
        rs += [sor]

    rno = 0
    for row in rs:
        cno = 0
        for char in row:
            if char == '#':
                
                if cno+1<c and rno+1<r and rs[rno][cno+1] == '#' and rs[rno+1][cno] == '#' and rs[rno+1][cno+1]=='#':
                    rs[rno][cno] = '/'
                    rs[rno][cno+1]= '\\'
                    rs[rno+1][cno]= '\\'
                    rs[rno+1][cno+1]='/'
                else:
                    sol = "Impossible"

            cno+=1
        rno+=1
            




    print "Case #"+str(i)+":"
    if len(sol)>0:
        print sol
    else:
        for rn in rs:
            ln = ""
            for ch in rn:
                ln+=ch
            print ln
    



    
    
    
