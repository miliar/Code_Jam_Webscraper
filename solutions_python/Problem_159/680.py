f = open("A-large.in")

o = open("a_large.out", "w+")


line = f.readline()
T = int(line[:-1])

for rep in range(T):
    line = f.readline()
    line = line[:-1] if line[-1] == '\n' else line
    N = line
    
    line = f.readline()
    line = line[:-1] if line[-1] == '\n' else line
    m = [int(i) for i in line.split(" ")]
    
    eaten = 0
    maxdif = 0
    prev = m[0]
    for i in m[1:]:
#        print("->prev:", prev, "cur:", i, "eaten:", eaten, "maxdif:", maxdif)
        if i < prev:
            eaten += prev-i
        if prev-i > maxdif:
            maxdif = prev-i
#        print("<-prev:", prev, "cur:", i, "eaten:", eaten, "maxdif:", maxdif)
        prev = i
        

    constantspeed = 0
#    print("maxdif is", maxdif)
    for i in m[:-1]:
        if i > maxdif:
#            print("[1]adding ", maxdif)
            constantspeed += maxdif
        else:
#            print("[2]adding ", i)
            constantspeed += i
        
#    print("Case #%d: %s %s\n"%(rep+1, eaten, constantspeed))
    o.write("Case #%d: %s %s\n"%(rep+1, eaten, constantspeed))
o.close()
f.close()
