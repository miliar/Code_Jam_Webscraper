import time

start_time = time.time()

def find(r, k, n, g):
    # run r times with k people, n groups of g[i] people
    pos = 0 # current position in line
    people = 0 # people on roller coaster
    total = 0 # total made    
    c = 0 # current groups gone through
    
    for i in range(r):
        while people + g[pos] <= k and c < n:
            # print "  Group of %d enters. People was %d, now is %d" % (g[pos], people, people+g[pos])
            people += g[pos]
            pos = (pos+1) % n
            c += 1

        total += people
        people = 0
        c = 0

    return total




f = open("C-small-attempt0.in", "r")
f2 = open("C-small-attempt0.out", "w")

try:
    T = int(f.readline().strip())

    lines = f.readlines()

    r = k = n = 0
    g = []
    for i in range(0, T):
        [r, k, n] = map(int, lines[2*i].strip().split(" "))
        g = map(int, lines[2*i+1].strip().split(" "))
                
        s = "Case #%d: %d\n" % (i+1, find(r, k, n, g))
        f2.write(s)

    f2.flush()
     
except Exception, ex:
    print ex
    
finally:
    f.close()
    f2.close()

print "time = %f seconds" % (time.time() - start_time)
