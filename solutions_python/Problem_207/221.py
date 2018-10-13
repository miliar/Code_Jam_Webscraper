def solve(line):
    l = line.split(" ")
    N = int(l[0])
    r = int(l[1])
    o = int(l[2])
    y = int(l[3])
    g = int(l[4])
    b = int(l[5])
    v = int(l[6])
    m = min([r,y,b])
    r-=m
    y-=m
    b-=m
    out = ""
    if r==0:
        m2 = min(y,b)
        y -= m2
        b -= m2
        if y==0:
            out += m2*"YB"
            if b>m:
                return "IMPOSSIBLE"
            else:
                out += b*"RBYB" + (m-b)*"RYB"
        else:
            out += m2*"BY"
            if y>m:
                return "IMPOSSIBLE"
            else:
                out += y*"RYBY" + (m-y)*"RBY"
            
    elif y==0:
        m2 = min(r,b)
        r -= m2
        b -= m2
        if r==0:
            out += m2*"RB"
            if b>m:
                return "IMPOSSIBLE"
            else:
                out += b*"RBYB" + (m-b)*"RYB"
        else:
            out += m2*"BR"
            if r>m:
                return "IMPOSSIBLE"
            else:
                out += r*"BRYR" + (m-r)*"BYR"
    else:
        m2 = min(r,y)
        r -= m2
        y -= m2
        if r==0:
            out += m2*"RY"
            if y>m:
                return "IMPOSSIBLE"
            else:
                out += y*"RYBY" + (m-y)*"RYB"
        else:
            out += m2*"YR"
            if r>m:
                return "IMPOSSIBLE"
            else:
                out += r*"BRYR" + (m-r)*"BYR"
        
    
        
    return out
	
import sys
filename = sys.argv[1]
f = open(filename, "r")
s = f.read()
f.close()
lines = s.split("\n")
lines = [l.strip() for l in lines]
T = int(lines[0])
k=1
for i in range(T+1):
    if i==0:
        continue
    #N = int(lines[k].split(" ")[1])
    #print lines[k:k+N+1]
    ans = solve(lines[i])
    #k+=N+1
    print "Case #"+str(i)+": "+ans