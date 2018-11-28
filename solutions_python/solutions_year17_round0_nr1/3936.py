def flipchars(chars, startpos, lenflipper,):
    lchars = list(chars)
    endpos = (startpos+lenflipper)
    if endpos > len(lchars):
        pass
    else:
        for lcharpos in range(startpos, endpos):
            if lchars[lcharpos] == '+':
                lchars[lcharpos] = '-'
            else:
                lchars[lcharpos] = '+'
    return ''.join(lchars)


def neededflips(flipcount, maxflipcount, maxflipsize, flipstr, startpos=0):
    if not "-" in list(flipstr):
        return flipcount
    else:

        if len(flipstr) >= flipcount+1:
            flipstr = flipchars(flipstr, startpos, maxflipsize)
            flipcount += 1
            if "-" in list(flipstr):
                return neededflips(flipcount, maxflipcount, maxflipsize, flipstr, list(flipstr).index("-"))
            else:
                #print (flipstr)
                return flipcount
        else:
            return 'IMPOSSIBLE'

t = int(input())
for i in range(1, t + 1):
    toflipstring, m = input().split(" ")
    maxflipsize = int(m)
    flipcount = 0
    #for xi in range(0, len(toflipstring)-maxflipsize):
    if '-' in list(toflipstring):
        flipcount = neededflips(flipcount, len(toflipstring)-maxflipsize, maxflipsize, toflipstring, list(toflipstring).index("-"))
    print("Case #{}: {}".format(i, flipcount))