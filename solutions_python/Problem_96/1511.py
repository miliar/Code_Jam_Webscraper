f = open("B-large.in")
lines = f.readlines()
f.close()

lines.pop(0)
case = 1
for line in lines:
    line = line.replace("\n", "").split(" ")
    line.pop(0)
    s = int(line.pop(0))
    t = int(line.pop(0))
    # print s, t
    
    ret = 0
    for i in line:
        i = int(i)
        m = (i / 3) + (0 if (i % 3 == 0) else 1)
        # print i, m, t
        if m >= t:
            ret += 1
        elif i > 0:
            if (i % 3 != 1) and (m+1 == t) and s > 0:
                ret += 1
                s -= 1
    
    print "Case #%i: %s" % (case, str(ret))
    case += 1