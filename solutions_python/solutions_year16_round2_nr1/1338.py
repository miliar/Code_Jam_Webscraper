def getNumber(string):
    num = -1
    if "Z" in string:
        num = 0
        string = string.replace("Z","",1)
        string = string.replace("E","",1)
        string = string.replace("R","",1)
        string = string.replace("O","",1)
    elif "X" in string:
        num = 6
        string = string.replace("S","",1)
        string = string.replace("I","",1)
        string = string.replace("X","",1)
    elif "W" in string:
        num = 2
        string = string.replace("T","",1)
        string = string.replace("W","",1)
        string = string.replace("O","",1)
    elif "U" in string:
        num = 4
        string = string.replace("F","",1)
        string = string.replace("O","",1)
        string = string.replace("U","",1)
        string = string.replace("R","",1)
    elif "G" in string:
        num = 8
        string = string.replace("E","",1)
        string = string.replace("I","",1)
        string = string.replace("G","",1)
        string = string.replace("H","",1)
        string = string.replace("T","",1)
    elif "F" in string:
        num = 5
        string = string.replace("F","",1)
        string = string.replace("I","",1)
        string = string.replace("V","",1)
        string = string.replace("E","",1)
    elif "V" in string:
        num = 7
        string = string.replace("S","",1)
        string = string.replace("E","",1)
        string = string.replace("V","",1)
        string = string.replace("E","",1)
        string = string.replace("N","",1)
    elif "O" in string:
        num = 1
        string = string.replace("O","",1)
        string = string.replace("N","",1)
        string = string.replace("E","",1)
    elif "N" in string:
        num = 9
        string = string.replace("N","",1)
        string = string.replace("I","",1)
        string = string.replace("N","",1)
        string = string.replace("E","",1)
    elif "T" in string:
        num = 3
        string = string.replace("T","",1)
        string = string.replace("H","",1)
        string = string.replace("R","",1)
        string = string.replace("E","",1)
        string = string.replace("E","",1)
    return (num, string)

def solve_N(string):
    nums = []
    while not string == "":
        num, string = getNumber(string)
        nums.append(num)
    return "".join(map(str, sorted(nums)))

def solve(Ns):
    for i in range(len(Ns)):
        print "Case #"+str(i+1)+": "+solve_N(Ns[i])

def parse(filename):
    f = open(filename)
    lines = f.readlines()
    num_inputs = int(lines[0])
    inputs = []
    for x in range(num_inputs):
        inputs.append(lines[x+1].strip())
    solve(inputs)

parse("A-large.in")
