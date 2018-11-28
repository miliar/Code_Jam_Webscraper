#!/usr/bin/python

def main():
    fin = open('A-small-attempt1.in', 'r')
    fout = open('magic.out', 'w')

    fin.seek(0)
    ncases = int(fin.readline())

    for i in range(1, ncases + 1):
        fout.write("Case #" + str(i) + ": ")
        row1 = int(fin.readline().strip())
        cards1 = set([int(i) for i in readrelline(fin, row1).strip().split()])
        if row1 < 4:
            readrelline(fin, 4 - row1)
        row2 = int(fin.readline().strip())
        cards2 = set([int(i) for i in readrelline(fin, row2).strip().split()])
        if row2 < 4:
            readrelline(fin, 4 - row2)
        possible = cards1 & cards2
        if len(possible) == 1:
            fout.write(str(possible.pop()) + "\n")
        elif len(possible) > 1:
            fout.write("Bad magician!\n")
        else:
            fout.write("Volunteer cheated!\n")

def readrelline(f, line):
    for i in range(line - 1):
        f.readline()
    return f.readline()

if __name__ == "__main__":
    main()
