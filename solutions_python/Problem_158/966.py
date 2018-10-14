
inputData = """4
2 2 2
2 1 3
4 4 1
3 2 3"""

inputData = open("C:/Documents and Settings/Yury/Downloads/D-small-attempt0.in").read()
#inputData = open("C:/Documents and Settings/Yury/Downloads/D-large.in").read()

def calculate(text):
    X, R, C = [int(x) for x in text.split()]
    
    if (R * C) % X != 0:
        return "RICHARD"

    if X >= 3:
        if R <= X - 2 or C <= X - 2:
            return "RICHARD"
    if X > R and X > C:
        return "RICHARD"

    return "GABRIEL"

def parse(text):
    array = text.split("\n")
    ncases = int(array[0])
    output = []
    for i in range(ncases):
        output.append("Case #%d: %s" % (i+1, calculate(array[i+1])))
    open("out.txt", "wb").write("\n".join(output))
    print "\n".join(output)

parse(inputData)

