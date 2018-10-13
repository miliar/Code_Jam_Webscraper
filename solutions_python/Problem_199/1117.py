f = open("A-large.in", 'r')
numtests = f.readline()
inputs = []

for line in f:
    inputs.append(line)

def solve1():
    f2 = open("output.txt", 'w')
    casen = 0
    for inp in inputs:
        casen = casen+1
        inp = inp.strip()
        inps = inp.split(' ')
        pan = inps[0]
        n = int(inps[1])
        count = 0
        if (n > len(pan)):
            success = False
        elif (n == 0):
            success = False
        else:
            for i in range(len(pan) - n + 1):
                if (pan[i] == '-'):
                    for j in range(n):
                        if (pan[i+j] == '-'):
                            pan = pan[:i+j] + "+" + pan[i+j+1:]
                        else:
                            pan = pan[:i+j] + "-" + pan[i+j+1:]
                    count = count+1
            success = True
        for c in pan:
            if (c != '+'):
                success = False
        if (success):
            f2.write("Case #" + str(casen) + ": " + str(count) + "\n")
        else:
            f2.write("Case #" + str(casen) + ": IMPOSSIBLE\n")
    f2.close()

solve1()
f.close()
