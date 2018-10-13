f = open("C:\LARGE.TXT")

lines = []
line = ""
for line in f:
    lines.append( line.replace("\n", ""))

times = int(lines[0])
lines = lines[1:]

j = 1
for i in range(times):
    v1 = [int(x) for x in lines[1].split(" ")]
    v2 = [int(x) for x in lines[2].split(" ")]

    v1.sort()
    v2.sort()
    v2 = v2[::-1]
    sum = 0
    for i, x in enumerate(v1):
        sum += v1[i]*v2[i]
        
    print "Case #" + str(j) + ": " + str(sum)
    
    lines = lines[3:]
    j += 1