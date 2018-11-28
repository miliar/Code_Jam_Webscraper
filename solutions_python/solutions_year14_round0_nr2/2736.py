inp = open('B-large.in', 'r')
out = open('B-large.out', 'w')

cases = int(inp.readline().strip())

for r in range(cases):
    line = inp.readline().strip() + ' '
    a = line.split()
    c = float(a[0])
    f = float(a[1])
    x = float(a[2])
    
    cps = 2.0
    time = 0.0
    buyFarm = True

    if c > x:
        time = x / cps
        buyFarm = False

    while buyFarm == True:
        time += c / cps

        if (x-c)/cps > x/(cps+f):
            cps += f
        else:
            time += (x-c)/cps
            buyFarm = False

    out.write("Case #" + str(r+1) + ": " + str(time) + "\n")
        

inp.flush()
out.flush()
inp.close()
out.close()
