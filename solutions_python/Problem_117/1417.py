f = open("input.txt","r")
t = int(f.readline())
out = open("output.txt","w")

def check(lawn,x,y):
    for j in xrange(x):
        for k in xrange(y):
            fl = 0
            flag = 0
            cur = lawn[j][k]
            for p in xrange(x):
                if lawn[p][k] > cur:
                    flag = 1
                    break
            for p in xrange(y):
                if lawn[j][p] > cur:
                    fl = 1
                    break
            if fl == 1 and flag == 1:
                return False
    return True    

for a in xrange(t):
    x,y = map(int,f.readline().split())
    lawn = []
    for j in xrange(x):
        lawn.append(map(int,f.readline().split()))
    ans = 0
    if check(lawn,x,y):
        wr = "Case #" + str(a+1) + ": YES\n"
    else:
        wr = "Case #" + str(a+1) + ": NO\n"
    out.write(wr)
f.close()
out.close()
    
            
        
