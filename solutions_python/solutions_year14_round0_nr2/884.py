fin = open("input.in", "r")
fout = open("output.txt" , "w")
file = fin.read().split("\n")
file.pop(0)
for count, line in enumerate(file):
    rate = 2
    time = 0
    cookie = 0
    cost, gain, target = [float(x) for x in line.split()]
    if cost < target:
        while cookie < target:
            cookie += cost
            time += cost/rate
            #print (((target - cookie)/rate), (target)/(rate+gain))
            if ((target - cookie)/rate) > (target)/(rate+gain):
                cookie -= cost
                rate += gain
            else:
                time += (target - cookie)/rate
                cookie = target
            #print (cookie, time, rate, gain)
    else:
        time = target/rate
    fout.write("Case #%d: %s\n" %(count + 1, time))
fout.close()
fin.close()
