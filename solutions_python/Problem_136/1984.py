
file = open("B-large (1).in")

t = file.next()
for test_case in xrange(1, int(t)+1):
    row = [float(x.rstrip()) for x in file.next().split(" ")]
    c = row[0] # cookie cost
    f = row[1] # cookies per second gain
    x = row[2] # goal number of cookies

    rate = 2.0
    last_time = 0.0
    while True:
        no_farm_time = x/rate
        next_no_farm_time = c/rate + x/(rate+f)
        if no_farm_time < next_no_farm_time:
            last_time += no_farm_time
            break
        last_time += c/rate
        rate += f

    print "Case #" + str(test_case) + ": " + str(last_time)
