f = open("C:/Users/Eric/dropbox/codejam/cookie-large.in")

lines = f.readlines()[1:]

num = 1

for line in lines:
    c,f,x = [float(n) for n in line.split()]
    t = 0
    farms = 0
    while c/(2+f*(farms)) + (x)/(2+f*(farms+1)) < (x)/(2+f*(farms)):
        t += c/(2+f*(farms))
        farms += 1
    t += (x)/(2+f*(farms))
    print "Case #%d: %s" % (num, t)
    num += 1
