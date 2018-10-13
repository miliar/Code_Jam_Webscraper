from math import ceil

inf = open("input.txt", "r")
ouf = open("out.txt", "w")
for i in range(int(inf.readline())):
    x, a, b = map(int, inf.readline().split())
    
    if x > 6 or x > max(a, b) or ceil(x ** 0.5) > min(a, b) or (a * b) % x:
        ouf.write("Case #" + str(i + 1) + ": RICHARD\n")
    else:
        ouf.write("Case #" + str(i + 1) + ": GABRIEL\n")

inf.close()
ouf.close()