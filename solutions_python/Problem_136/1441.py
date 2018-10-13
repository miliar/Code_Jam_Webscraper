fin  = open("B-large.in", "r")
fout = open("output.txt", "w")

t = int(fin.readline()[:-1])
i = 0

while i < t :
    info = list(map(float,fin.readline().split()))
    c = info[0]
    f = info[1]
    x = info[2]
    buy = True
    time = 0
    rate = 2
    
    i += 1
    while buy :
        not_buy = x / rate
        buy = (c / rate) + (x / (rate + f))

        if buy < not_buy :
            buy = True
            time += c /rate
            rate += f
        else:
            time += x / rate
            buy = False
            break
    fout.write("Case #" + str(i) + ": " + str(round(time,10)) + '\n')
fout.close()
