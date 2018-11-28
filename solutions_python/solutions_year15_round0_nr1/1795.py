
tests = int(raw_input())
for t in range(tests):
    line = raw_input()
    Smax, info = line.split(" ")
    Smax = int(Smax)
    l = list(info)
    total = int(l[0])
    extra = 0
    
    for index in range(1, Smax):
        #print(total, index)
        if(l[index]=="0"):
            continue
        
        while(total<index):
            #print("-", total, index)
            total +=1
            extra +=1
        total += int(l[index])
        
    missing = Smax - total
    
    if (missing > 0):
        extra += missing
    print("Case #%d: %d" % (t+1, extra))
    

    