def end_time(destination, position, speed):
    h = float(destination - position) / speed
    hh = float(destination / h)
    return hh

# f = open("a.txt", "r").readlines()
f = open("A-large.in", "r").readlines()
T = f.pop(0).strip()
output = open("wc1.txt", "w")
start = True
speed = None
case = 1
for line in f:
    x, y = [int(x) for x in line.strip().split(" ")]
    if start:
        destionation = x
        horses = y
        start = False
    else:
        kmh = end_time(destionation, x, y)
        if not speed or kmh < speed:
            speed = kmh
        horses -= 1
    if horses == 0:
        start = True
        
        print "Case #%s: %s" % (case, speed)
        output.write("Case #%s: %s\n" % (case, speed))
        speed = None
        case += 1
output.close()