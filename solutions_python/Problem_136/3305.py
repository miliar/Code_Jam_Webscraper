def cookieClicker(c,f,x):
    speed = 2
    times = []
    while 1:
        if x/speed <= (c/speed + x/(speed+f)):
            times.append(x/speed)
            return sum(times)
        times.append(c/speed)
        speed += f
input1 = open('B-large.in','r').read()
lines = input1.split('\n')[1:]
for j, line in enumerate(lines):
    line = line.split()
    c,f,x = (float(i) for i in line)
    print "Case #{0}: {1}".format(j+1,cookieClicker(c,f,x))
