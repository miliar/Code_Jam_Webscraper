import math

def wellShit(best, cps, saved, time, c, f, x):
    while True:
        a = (x - saved) / cps
        b = (c - saved) / cps
        if a < b:
            best = a + time
            break
        if best < time + b or best < time + a:
            break
        best = time + a
        cps = cps + f
        saved = 0.0
        time = time + b
        
    return best



inputs = open("in.txt").readlines()
output = open('out.txt', 'w')
t = int(inputs[0])
for i in range(1, t + 1):
    num = inputs[i].rstrip().split(" ")
    c = float(num[0])
    f = float(num[1])
    x = float(num[2])
    output.write("Case #%d: %.7f\n"%(i,wellShit(x / 2.0, 2.0, 0.0, 0.0, c, f, x)))
output.close()
