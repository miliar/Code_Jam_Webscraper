import math

def check(i):
    s = str(i)[::-1]
    j = int(s)
    if j == i:
        return True
    else:
        return False

def count(a, b):
    start = int(math.sqrt(a))
    end = int(math.sqrt(b+1))
    c = 0
    for i in range(start, end + 1):
        if a <= i * i <= b and check(i) and check(i*i):
            c += 1
    return c

f = open("C-small-attempt2.in", "r")
out = open("C-small.out", "w")
line = f.readline()
T = int(line)
for i in range(0, T):
    line = f.readline()
    line = line.split(" ")
    A = int(line[0])
    B = int(line[1])
    result = count(A, B)
#    print "Case #%d: %s" %(i+1, result)
    out.write("Case #%d: %s\n" %(i+1, result))
f.close()
out.close()
