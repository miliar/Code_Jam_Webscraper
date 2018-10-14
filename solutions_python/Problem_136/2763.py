file = open("input.txt", "rU")
cases = int(file.readline().strip())
results = ""
for case in range(cases):
    line = file.readline().split()
    c = float(line[0])
    f = float(line[1])
    x = float(line[2])
    rate = 2.0
    total_time = c/rate
    while True:
        if (x/(rate+f)) < ((x-c)/rate):
            rate += f
            total_time += c/rate
        else:
            total_time += ((x-c)/rate)
            results += "Case #" + str(case+1)
            results += ": {0:.7f}\n".format(total_time)
            break
    
file.close()
results = results.strip()

out = open("output.txt", "w")
out.write(results)
out.close()
