
f = open("B-large.in")
out = open("output.txt", "w")
T = int(f.readline())

for t in range(T):
    C, F, X = map(float, f.readline().split(" "))
    cper = 2.0
    sum = 0
    
    while 1:
        if X/cper < C/cper + X/(cper+F):
            sum += X/cper
            break
        sum += C/cper
        cper += F
        
    out.write("Case #%d: %.7f\n" %(t+1, sum))
        
    