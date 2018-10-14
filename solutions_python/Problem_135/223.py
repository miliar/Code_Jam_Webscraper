import sys, copy;

a1, a2 = 0, 0
d1, d2 = [[]]*2

def solve():
    s1 = set(d1[a1 - 1]);
    s2 = set(d2[a2 - 1]);
    s = s1 & s2
    l = len(s)
    return s.pop() if l == 1 else "Volunteer cheated!" if l == 0 else "Bad magician!";

inputFile =  sys.argv[1] if (len(sys.argv) > 1) else "input.txt";
outputFile = sys.argv[2] if (len(sys.argv) > 2) else (inputFile + "out.txt") if (len(sys.argv) > 1) else "output.txt";
print inputFile, outputFile
file = open(outputFile, "w")

with open(inputFile, 'r') as f:
    t = int(f.readline())
    print t
    for i in range(1, t + 1):
        file.write("Case #" + str(i) + ": ")
        a1 = int(f.readline())
        print a1
        d1 = [[0 for x in xrange(4)] for x in xrange(4)]
        d2 = [[0 for x in xrange(4)] for x in xrange(4)]
        for j in range(4):
            d1[j] = map(int, f.readline().split())
        print d1
        a2 = int(f.readline())
        print a2
        for j in range(4):
            d2[j] = map(int, f.readline().split())
        print d2
        file.write(str(solve()) + "\n")
file.close()            








