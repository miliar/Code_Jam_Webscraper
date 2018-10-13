

    
def ride(max, groups):
    
    c = 0
    
    rode = []

    while c <= max:
        
        if groups[0] + c <= max:
            rode = groups.pop(0)
            c = c + groups.pop(0)
        else:
            break

    return c


f = open('sample.in','r')

lines = []

while f:
    
    line = f.readline().replace("\n","").replace("\r","")

    if len(line) == 0:
        break

    lines.append(line)

f.close()


T = int(lines[0])

t = 0

out = []

while t < (T*2):
    
    t = t + 1
    
    p = lines[t].rsplit(" ")

    R = int(p[0])
    k = int(p[1])
    N = int(p[2])

    t = t + 1

    g = map(int,lines[t].rsplit(" "))

    ####
   

    r = 0
    i = 0
    c = 0
    e = 0
    s_i = 0 


    while r < R:
        
        while g[i] + c <= k:
            c = c + g[i]
            i = i + 1
            if i >= len(g):
                i = 0
            if s_i == i:
                break
        e = e + c
        c = 0 
        r = r + 1
        s_i = i

    
    o =  "Case #%s: %s\n" % ((t/2),e)
    print o
    out.append(o)

f = open("result.out","w")

for l in out:
    f.write(l)

f.close()
