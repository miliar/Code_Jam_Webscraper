fo = open("B-large.in", "r")
f = open("B-large.out", "w")
lines=fo.readlines()
cases = int(lines[0])

for n in range(0, cases):
    
    array = lines[n+1].split(' ')
    C = float(str(array[0]))
    F = float(str(array[1]))
    X = float(str(array[2]))
    cookies = 0
    cookierate = 2
    testtime = float(C)/float(F)
   
    


    T = float(0)
    
    while cookies < X:
        timeneeded = (float(C)/float(cookierate))
        if ((cookierate+F)*testtime < X):
            T = T+float(C)/float(cookierate)
            cookierate = cookierate + F
        else:
            T = T+float(X)/float(cookierate)
            cookies = X
            
            
    if n != cases-1:
        f.write("Case #{}: {}\n".format(n+1, T))
    else:
        f.write("Case #{}: {}".format(n+1, T))
            
    
    



fo.close()
f.close()