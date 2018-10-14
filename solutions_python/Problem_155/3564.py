t=int(input())
for x in range(t):
    noa = 0
    bnoa = 0
    g = input()
    gl = g.split()
    gli = []
    for r in gl[1]:
        gli.append(int(r))
    for h in gli:
        bnoa = bnoa + h
    for y in range(len(gli)):
        if y <= noa:
            noa=noa+gli[y]
        else:
            noa = y + gli[y]
    print("Case #"+str(x+1)+": "+str(noa - bnoa))
            
                
            
    
    
        
