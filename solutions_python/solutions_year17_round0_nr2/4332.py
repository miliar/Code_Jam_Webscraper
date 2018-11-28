import sys

def my_print(text):
    sys.stdout.write(str(text) + "\n")
    sys.stdout.flush()

name = "A-small"

fi = open(name + ".in")
lines = fi.readlines()
sys.stdout = open(name + ".out", "w")

testCases = int(lines[0])

for testCase in range(1, testCases + 1):
    line = lines[testCase]
    line = line.split()[0]
    n = int(line)
    line = list(map(int, list(line)))
    for i in range(len(line)-1):
        f = False
        d = False
        if line[i] > line[i+1]:
            for ii in range(1, i+1):
                if line[i] != line[i-ii]:
                    if ii == 1:
                        break
                    i = i-ii+1
                    break
                elif ii == i:
                    i = 0
            line[i] -= 1
            line = line[:i+1] + (len(line)-i-1) * [9]
            break
    line = list(map(str, line))
    line = ''.join(line)
    line = int(line)
    my_print("Case #" + str(testCase) + ": " + str(line))
fi.close()