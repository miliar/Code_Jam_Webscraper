import time

def test(n, k):
    is_on = (k+1) % (2**n) == 0
    if is_on:
        return "ON";
    else:
        return "OFF"

f = open("A-large.in", "r")
f2 = open("A-large.out", "w")

try:
    lines = f.readlines()
    T = int(lines[0].strip())

    line = []
    for i in range(1, T+1):
        line = map(int, lines[i].strip().split(" "))
        s = "Case #%d: %s\n" % (i, test(line[0], line[1]))
        f2.write(s)

    f2.flush()
     
except Exception, ex:
    print ex
    
finally:
    f.close()
    f2.close()
