def do(t):
    index = t+1
    found = False
    
    for i in xrange(t,t+k):
        if cake[i]=="+":
            cake[i] = "-"

            if not found:
                found = True
                index = i
                
        else:
            cake[i] = "+"

    return index

cases = int(raw_input())

for _ in xrange(cases):
    cake, k = raw_input().split()
    k = int(k)
    cake = list(cake)
    count = 0
    x = 0

    while(x<len(cake)-k+1):
        if cake[x]=="-":
            x = do(x)
            count += 1
        else:
            x += 1
            
    for i in xrange(len(cake)-k+1, len(cake)):
        if cake[i]=="-":
            print "Case #" + str(_+1) + ": IMPOSSIBLE"
            break
    else:
        print "Case #" + str(_+1) + ": " + str(count)
        
