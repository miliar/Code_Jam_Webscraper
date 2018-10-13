import copy
RUNNAME = "A-large"
INFILE = open(RUNNAME+".in","r")
OUTFILE = open(RUNNAME+".out","w")

# Turn a number as a string into a number
def magic(inthing):
    if inthing.isdigit():
        return int(inthing)
    try:
        return float(inthing)
    except ValueError:
        return inthing
    
# Get the data on the next line of the input file
def cj_getline():
    line = INFILE.readline().strip()
    lineparts = line.split(" ")
    parts = [magic(linepart) for linepart in lineparts]
    return parts

numcases = cj_getline()[0]
for caseno in range(numcases):
    N = cj_getline()[0]
    rows = []
    for rowno in range(N):
        row = []
        rawrow = INFILE.readline().strip()
        for char in rawrow:
            if char == '1':
                row.append(True)
            else:
                row.append(False)
        rows.append(row)
    swaps = 0
    while len(rows) > 1:
        for row in rows:
            row.pop(0)
        for ix, row in enumerate(rows):
            #Next row to move up to top?
            if not True in row:
                swaps += ix
                rows.pop(ix)
                break
    
    outstr = "Case #" + str(caseno+1) + ": " + str(swaps)
    print outstr
    OUTFILE.write(outstr+"\n")

INFILE.close()
OUTFILE.close()