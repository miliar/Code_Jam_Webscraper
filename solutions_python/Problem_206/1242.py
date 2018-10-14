inputfile = open("h2.in", mode='r')
outputfile = open("output_h_l.txt", mode='w')
t = int(inputfile.readline().strip())

for case in range(t):
    d, n = map(int, inputfile.readline().strip().split(' '))
    time = 0
    for i in range(n):
        hD, hS = map(int, inputfile.readline().strip().split(' '))
        hT = (d - hD) / hS
        if hT > time:
            time = hT
    speed = d / time
    outputfile.write("case #" + str(case + 1) + ": " + str(speed)+"\n")
    print("case #" + str(case + 1) + ": " + str(speed))
outputfile.close()
inputfile.close()
