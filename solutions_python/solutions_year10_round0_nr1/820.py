f = open("a.in")
content = f.readlines()

T = int(content[0])
w = open("a.out", "w")
for i in xrange(1, T+1):
    line = content[i].split(" ")
    N = int(line[0])
    K = int(line[1])
    
    mask = 0
    a = "ON"
    
    for j in range(0, N): 
        if K & (1 << j) == 0:
            a = "OFF"
    w.write("Case #%d: %s \n" % (i,a))

w.close()
raw_input()
    
    