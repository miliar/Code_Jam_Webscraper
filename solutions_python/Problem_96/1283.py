f = open('B-large.in', 'r')
o = open('B-large.out', 'w')

num = int(f.readline())

for x in range(0,num):
    a = f.readline()
    b = a.split(" ")
    for s in range(0,len(b)):
        b[s] = int(b[s])
    num_dancers = b[0]
    num_surprise = b[1]
    p = b[2]
    dancers = b[3:]
    total = 0
    for s in dancers:
        if s >= (3*p - 2):
            total += 1
        elif (s >= max(0,(3*p - 4))) and (num_surprise > 0) and (s >= 2):
            total += 1
            num_surprise -= 1
    o.write("Case #" + str(x+1) + ": " + str(total) + "\n")
    
f.close()
o.close()
