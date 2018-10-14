def run():
    output = open("output",'w')
    input = open("input")
    line = input.readline()
    tatal = int(line)
    line = input.readline()
    count = 1
    while line:
        tempstr = line.split()
        C = float(tempstr[0])
        F = float(tempstr[1])
        X = float(tempstr[2])
        mycost = 0.0
        V = 2.0
        while 1:
            if X<C or (X-C)/V < X/(F+V):
                mycost += X/V
                break;
            else:
                mycost += C/V
                V += F
        output.write("Case #"+str(count)+": "+str('%.7f' % mycost)+"\n")
        count += 1
        line = input.readline()
    output.close()
    input.close()

if __name__ == "__main__":
    run()
