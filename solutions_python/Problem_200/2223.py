n = int(raw_input())
for i in range(n):
    x = raw_input().strip()
    if len(x)==1:
        print "Case #"+str(i+1)+": "+x
        continue
    
    x = list(x)
    for ptr in range(len(x)-1, 0, -1):
        if x[ptr] >= x[ptr-1]:
            continue
        
        
        for j in range(ptr, len(x)):
            if x[j] == "9":
                break
            x[j] = "9"
        x[ptr-1] = chr(ord(x[ptr-1])-1)
    
    print "Case #"+str(i+1)+":", int("".join(x))