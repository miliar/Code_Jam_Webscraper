import sys, string

def magician(row1, row2):
    s1 = set(row1)
    s2 = set(row2)
    s = s1 & s2
    if len(s) > 1:
        return "Bad magician!"
    if len(s) == 0:
        return "Volunteer cheated!"
    return s.pop()

def main(args):
    f = file(args[1])
    ncases = int(f.readline())
    for i in range(ncases):
        line = f.readline()
        line = line.rstrip()
        nrow = int(line)
        for j in range(4):
            line = f.readline()
            if j+1 == nrow:
                line = line.rstrip()
                row1 = map(int, line.split(" "))
        line = f.readline()
        line = line.rstrip()
        nrow = int(line)
        for j in range(4):
            line = f.readline()
            if j+1 == nrow:
                line = line.rstrip()
                row2 = map(int, line.split(" "))
        ans = magician(row1, row2)
        sys.stdout.write("Case #%d: %s\n" % (i+1, ans))

if __name__ == "__main__":
    main(sys.argv)