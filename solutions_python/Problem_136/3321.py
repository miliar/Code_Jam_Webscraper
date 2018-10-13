

def solvecase(farmcost, cookincrate, wincook):

    cookrate = 2.0
    restime = 0

    while 1:

        wintime = wincook / cookrate

        ttofarm = farmcost / cookrate

        nxtcookrate = cookrate + cookincrate

        nxtwintime = ttofarm + wincook / nxtcookrate

        if wintime <= nxtwintime:
            return restime + wintime
        else:
            restime += ttofarm
            cookrate = nxtcookrate


inp = open("B-large.in")
out = open("out.txt", 'w')

count = int(inp.readline())

args = []

for i in range(1, count + 1):
    args = inp.readline().split(' ')

    strres = 'Case #' + str(i) + ': ' + str(solvecase(float(args[0]), float(args[1]), float(args[2])))

    out.write(strres + '\n')