
def calcmoves(asize, motes):
#    print("CALCMOVES: ")
#    print(asize)
#    print(motes)
    while len(motes) > 0 and motes[0] < asize:
        asize += motes[0]
        motes = motes[1:]
    if len(motes) > 0:
        if asize > 1:
            return 1 + min(calcmoves(asize, [asize - 1] + motes),
                           calcmoves(asize, motes[1:]))
        else:
            return 1 + calcmoves(asize, motes[1:])
    return 0

inputfile = "A-small-attempt1.in"
outputfile = "osmos.out"

inp = open(inputfile, "r")
cases = int(str(inp.readline().strip()))
i = 1
out = open(outputfile, "w")

while i <= cases:
    asize, _ = [int(k) for k in str(inp.readline()).strip().split()]
    motes = sorted([int(k) for k in str(inp.readline()).strip().split()])
    moves = calcmoves(asize, motes)
    print(asize, motes, moves)
    out.write("Case #" + str(i) + ": " + str(moves) + "\n")
    i += 1
