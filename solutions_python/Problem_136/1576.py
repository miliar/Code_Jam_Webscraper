text = open("cookie.in", "rb")
n = int(text.readline().strip("\n"))
for i in range(n):
    line = text.readline().strip("\n")
    line = line.split()
    c = float(line[0])
    f = float(line[1])
    x = float(line[2])
    maximum = f * (x - c) / c
    n = 2.0
    time = 0.0
    while(n < maximum):
        time += c / n
        n += f
    time += x / n
    output = open("cookie_answer.txt", "a")
    output.write("Case #" + str(i + 1) + ": " + "{0: .7f}".format(time) + "\n")
output.close()
text.close()
