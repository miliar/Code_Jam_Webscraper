iname = open(raw_input("File name: "), "r")
oname = open("out.txt", "w")

dat = iname.read().splitlines()
del dat[0]
count = 1

for i in xrange(0, len(dat)):
    print
    oname.write("Case #{}: ".format(count))
    count += 1

    values = dat[i].split()
    C = float(values[0])
    F = float(values[1])
    X = float(values[2])

    t = 0.0
    cF = 0

    while True:
        t_new = (C / (cF * F + 2))
        t_new_farm = t_new + (X / ((cF + 1) * F + 2))
        t_no_farm = X / (cF * F + 2)
        if t_new_farm < t_no_farm:
            t += t_new
            cF += 1
        else:
            t += t_no_farm
            oname.write("{:.7f}".format(t) + "\n")
            break
