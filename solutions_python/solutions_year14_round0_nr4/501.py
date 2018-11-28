iname = open(raw_input("File name: "), "r")
oname = open("out.txt", "w")

dat = iname.read().splitlines()
del dat[0]
count = 1

for i in xrange(0, len(dat), 3):
    oname.write("Case #{}: ".format(count))
    count += 1

    num = int(dat[i])
    nblocks = sorted([float(b) for b in dat[i + 1].split()])
    kblocks = sorted([float(b) for b in dat[i + 2].split()])
    onblocks = nblocks[:]
    okblocks = kblocks[:]

    p_opt = 0
    while onblocks:
        res = onblocks[0]
        for j in xrange(len(okblocks)):
            if res < okblocks[j]:
                del okblocks[j]
                break
        else:
            p_opt += 1
            del okblocks[0]
        del onblocks[0]

    p_dec = 0
    nblocks.reverse()
    kblocks.reverse()
    while nblocks:
        res = nblocks[0]
        for j in xrange(len(kblocks)):
            if res > kblocks[j]:
                del kblocks[j]
                del nblocks[0]
                p_dec += 1
                break
        else:
            del kblocks[0]
            del nblocks[len(nblocks) - 1]

    oname.write("{} {}\n".format(p_dec, p_opt))
