import sys
def check(ln1,ln2):
    return (ln1[0]< ln2[0])^(ln1[1] < ln2[1])
    
cases = int(sys.stdin.readline())
for i in range(1,cases+1):
    n = int(sys.stdin.readline())
    count = 0
    lines = []
    for j in range(n):
        lines.append([int(k) for k in sys.stdin.readline().split()])
    for t in range(n):
        for f in range(t+1,n):
            if(check(lines[t],lines[f])):
                count += 1
    print "Case #{0}: {1}".format(i,count)
        
        
        
     
