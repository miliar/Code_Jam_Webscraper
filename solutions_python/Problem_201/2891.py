def main():
    inputfile = open("C-small-1-attempt0.in", "r")
    f = open("small_output.txt", "w")
    filecontent = inputfile.read().splitlines()
    cases = int(filecontent[0])
    for x in range(1, cases + 1):
        total = int(filecontent[x].split(' ')[0])
        users = int(filecontent[x].split(' ')[1])
        if total==users:
            printval = ("Case #" + str(x) + ": " + str(0)+" "+ str(0))
            f.write(printval)
            f.write("\n")
            continue
        if users==1:
            if total%2==0:
                printval = ("Case #" + str(x) + ": " + str(int(total/2)) + " " + str(int(total/2)-1))
            else:
                printval = ("Case #" + str(x) + ": " + str(int(total / 2)) + " " + str(int(total / 2)))
            f.write(printval)
            f.write("\n")
            continue
        stalllist = [0 for xvar in range(total)]
        if total%2==1:
            stalllist[int(total / 2)] = 1
        else:
            stalllist[int(total / 2) - 1] = 1
        for xvar in range(2,users+1):
            i = 0
            fincnt = 0
            leftidx = -1
            rightidx = -1
            while i<total:
                count = 0
                if stalllist[i]==0:
                    lidx = i
                    while i< total and stalllist[i]==0:
                        count+=1
                        i+=1
                    ridx = i-1
                if count>fincnt:
                    fincnt=count
                    leftidx=lidx
                    rightidx=ridx
                i+=1
            if fincnt%2==0:
                insrtval = leftidx+int(fincnt/2)-1
            else:
                insrtval = leftidx + int(fincnt / 2)
            stalllist[insrtval] = 1
        lcnt = insrtval - 1
        rcnt = insrtval + 1
        ls = 0
        rs = 0
        while lcnt>=0:
            if stalllist[lcnt]==0:
                ls += 1
                lcnt -= 1
            else:
                break
        while rcnt<total:
            if stalllist[rcnt]==0:
                rs += 1
                rcnt += 1
            else:
                break
        y = max(ls,rs)
        z = min(ls,rs)
        printval = ("Case #" + str(x) + ": " + str(y) + " " + str(z))
        f.write(printval)
        f.write("\n")
    f.close()

if __name__ == '__main__':
    main()