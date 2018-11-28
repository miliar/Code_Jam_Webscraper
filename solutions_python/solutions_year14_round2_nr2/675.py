import sys, copy;

def solve():
    r = 0;
    #print 'a = ', a, 'b = ', b
    for i in range(0, a):
        for j in range(0, b):
            if i & j < k :
                #print i, j, i & j, k, i & j < k, r
                r = r + 1
    return r

inputFile =  sys.argv[1] if (len(sys.argv) > 1) else "input.txt";
outputFile = sys.argv[2] if (len(sys.argv) > 2) else (inputFile + "out.txt") if (len(sys.argv) > 1) else "output.txt";
print inputFile, outputFile
file = open(outputFile, "w")

with open(inputFile, 'r') as f:
    t = int(f.readline())
    print t
    for i in range(1, t + 1):
        file.write("Case #" + str(i) + ": ")
        a, b, k = map(int, f.readline().split())
        file.write(str(solve()) + "\n")
file.close()            








