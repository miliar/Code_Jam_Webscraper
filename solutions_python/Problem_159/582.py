from math import *


def main():
    inpfile = open("A-large.in", 'r')
    outfile = open('outfile', 'w')
    casenum = int(inpfile.readline().strip())
    for case in range(1, casenum + 1):
        line = inpfile.readline().strip()
        line2 = inpfile.readline().strip()
        linelst = line2.split()

        N = int(line)

        # print N
        # print linelst
        l = []
        for e in linelst:
            l.append(int(e))

        # print l
        min1 = 0
        speed = 0
        min2 = 0
        prev = -1
        for e in l:
            if prev == -1:
                prev = e
                continue
            if (prev - e) > 0:
                min1 += (prev - e)
            speed = max(speed, (prev - e))
            # print speed
            # print e
            prev = e
        
        # print speed

        for e in l[:-1]:
            if (e < speed):
                min2 += e
            else:
                min2 += speed
            # print min2
            

        result = "Case #" + str(case) + ": " + str(min1) + " " + str(min2) + "\n"
        print result
        outfile.write(result)
    inpfile.close()
    outfile.close()




if __name__ == "__main__":


    main()

    