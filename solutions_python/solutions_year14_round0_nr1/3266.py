def solve():
    input_file = "A-small-attempt0.in"
    output_file = "20140_A_small.out"

    ifile = open(input_file, 'r')
    ofile = open(output_file, 'w')

    T = int(ifile.readline())
    for i in range(T):
        ofile.write("Case #" + str(i+1) + ": ")
        n1 = int(ifile.readline())
        a1 = []
        a2 = []
        for j in range(4):
            s = ifile.readline().strip()
            if(n1 != (j+1)): 
                continue
            a1 = [int(k) for k in  s.split()]
        n2 = int(ifile.readline())
        for j in range(4):
            s = ifile.readline().strip()
            if(n2 != (j+1)): continue
            a2 = [int(k) for k in s.split()]

        count = 0
        tc = -1 
        for j in range(4):
            for k in range(4):
                if (a1[j] == a2[k]):
                    count = count + 1
                    tc = a1[j]
        if (count == 0):
            ofile.write("Volunteer cheated!\n")
        elif (count == 1):
            ofile.write(str(tc)+"\n")
        else:
            ofile.write("Bad magician!\n")


if __name__ == "__main__":
    solve()
