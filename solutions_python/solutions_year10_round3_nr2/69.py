import time, math
starttime = time.time()

f = open("B-large.in", "r")
f2 = open("B-large.out", "w")

try:
    T = int(f.readline().strip())
    
    for i in range(T):
        [l, p, c] = map(float, f.readline().strip().split(" "))

        mag = math.ceil(math.log(p/l, c))
        steps = 0
        while mag > 1:
            mag = math.ceil(mag/2)
            steps += 1

        s = "Case #%d: %d\n" % (i+1, steps)

        #print s,
        f2.write(s)
                
    f2.flush()
    
finally:
    f.close()
    f2.close()

print (time.time() - starttime)
