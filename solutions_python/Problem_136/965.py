fi = open("input.txt")
for testNum in range(int(fi.readline().strip())):
    cases = []
    c,f,x = tuple(float(i) for i in fi.readline().strip().split(" "))
    time=0
    cookies=0
    rate=2
    cases.append(x/2)
    current = (time+(x-c)/rate)
    while(current <= min(cases)):
        time += c/rate
        rate += f
        current = (time+(x)/rate)
        cases.append(current)
    print("Case #"+str(testNum+1)+": "+str(min(cases)))
        
        
        
    
    
    
    
