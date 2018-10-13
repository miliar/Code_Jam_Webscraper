file = open("A-large.in")
write = open("A-large.out","wb")

line = file.readline()
T = int(line)

for i in range(T):
    line = file.readline()
    line = line.split(" ")
    r = int(line[0])
    t = int(line[1])
    result = -(2*r-1)/4.0 + (((2*r-1)**2 + 8*t)**.5)/4.0
    result = int(result)
    while (2*result**2 + (2*r-1)*result < t):
        result +=1
    while (2*result**2 + (2*r-1)*result > t):
        result -=1
    write.write("Case #%d: %d\n" % (i+1,int(result)))
print "done"
