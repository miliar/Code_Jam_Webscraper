def read(f):
    return f.readline().strip()
with open("B-large.in") as infile:
    t = int(read(infile))
    for case in range(1,t+1):
        data = list(map(float,read(infile).split()))
        c,f,x = data
        seconds = 0
        rate = 2
        while x/rate > (c/rate + x/(rate+f)):
                seconds += (c/rate)
                rate += f
        seconds += x/rate
        print("Case #{}: {:.7f}".format(case, seconds))

