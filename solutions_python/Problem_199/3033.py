def flip(array, start, size):
    for h in range(start, start + size):
        if(array[h]=="-"):
            array[h] = "+"
        else:
            array[h] = "-"

with open("A-large.in") as file, open("output", "w") as fp:
    case = 1
    for i in range(1):
        cases = file.readline()
    for line in file:
        pancakes = list(line.split()[0])
        k = int(line.split()[1])
        j = 0
        s = 0
        solvable = True
        while(j < len(pancakes)):
            if(pancakes[j]=="-"):
                if(len(pancakes) - j < k):
                    solvable = False
                    break
                s += 1
                flip(pancakes, j, k)
            j += 1
        fp.write("Case #{}: ".format(case))
        if(solvable):
            fp.write(str(s))
        else:
            fp.write("IMPOSSIBLE")
        fp.write("\n")
        case += 1

