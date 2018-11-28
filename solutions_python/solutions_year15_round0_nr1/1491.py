


def main():
    inpfile = open("A-large.in", 'r')
    outfile = open('outfile', 'w')
    casenum = int(inpfile.readline().strip())
    for case in range(1, casenum + 1):
        line = inpfile.readline().strip()
        linelst = line.split()
        
        n = int(linelst[0])
        m = linelst[1]
        
        # print linelst
        acc = 0
        need = 0
        for i in range(int(n)+1):
            np = int(m[i])
            if acc < i:
                need += 1
                acc += 1
            # print np
            acc += np

        result = "Case #" + str(case) + ": " + str(need) + "\n"
        print result
        outfile.write(result)
    inpfile.close()
    outfile.close()




if __name__ == "__main__":


    main()

    