from decimal import *

def main():
    getcontext().prec = 30
    
    fin = open("B-large.in.txt", "r")
    fout = open("B-large.out.txt", "w")
    lines = int((fin.readline())[:-1])

    for i in range(lines):
        line = (fin.readline())[:-1].split()
        c, f, x = Decimal(float(line[0])), Decimal(float(line[1])), Decimal(float(line[2]))

        time = Decimal(0.0)
        rate = Decimal(2.0)
        while ((c / rate) + (x / (rate + f))) < (x / rate):
            time += (c / rate)
            rate += f
        time += (x / rate)

        fout.write("Case #" + str(i + 1) + ": " + str(float(time)) + "\n")

    fin.close()
    fout.close()

main()
