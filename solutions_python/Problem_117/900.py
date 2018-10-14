import re

# Method to get dimension of lawn recatangle
def rectdimens(fp):
    dims = re.split(" ",fp.readline())
    x,y = int(dims[1]), int(dims[0])    
    lawndimen = []
    for i in range(y):
        line = fp.readline()
        nums = [int(x.strip()) for x in re.split(" ",line)]
        lawndimen.append(nums)
    return lawndimen


# Method to check if pattern could be achieved or not
def check_status(lawnvalue):
    row_maxes = [max(x) for x in lawnvalue]
    cols = [[lawnvalue[i][j] for i in range(len(lawnvalue))] for j in range(len(lawnvalue[0]))]
    col_maxes = [max(x) for x in cols]
    for i in range(len(lawnvalue)):
        for j in range(len(lawnvalue[i])):
            val = lawnvalue[i][j]
            if val != row_maxes[i] and val != col_maxes[j]:
                return "NO"
    return "YES"


# Method for input and output of data.
def lawnmower():
    output = []
    with open("B-large.in","r") as fp:
        casecount = fp.readline()
        for i in range(int(casecount.strip())):
            state = rectdimens(fp)
            outline = "Case #%d: %s" % (i+1, check_status(state))
            print outline
            output.append(outline)
    with open("lawn_large_output.out","w") as fp:
        fp.write("\n".join(output))


if __name__ == "__main__":
    lawnmower()