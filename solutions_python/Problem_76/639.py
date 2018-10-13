def patsum(candylist):
    if len(candylist) == 0:
        return -1
    total = 0
    for i in candylist:
        total ^= int(i)
    return total
def realsum(candylist):
    total = 0
    for i in candylist:
        total += int(i)
    return total

def recurse(candy, a, b):
    if len(candy) == 0:
        suma = patsum(a)
        sumb = patsum(b)
        #print suma, sumb
        if (suma == sumb):
            #print a, b
            return max(realsum(a), realsum(b))
        else:
            return -1
    curr = candy[-1]
    candynew = candy[:-1]
    aplus = a[:]
    aplus.append(curr)
    atotal = recurse(candynew, aplus, b)

    bplus = b[:]
    bplus.append(curr)
    btotal = recurse(candynew, a, bplus)

    return max(atotal, btotal)

fin = file("C-small-attempt0.in", "rU")
fout = file("C-small-attempt0.out", "w")
ncases = int(fin.readline().strip())
for i in xrange(ncases):
    line = fin.readline()
    candy = fin.readline().strip().split()
    candy.sort()
    '''totalxor = 0
    for i in candy:
        totalxor ^= int(i)
    print totalxor #if not zero, impossible to split'''
    sean = recurse(candy, [], [])
    if sean == -1:
        sean = "NO"
    strout = "Case #" + str(i+1) + ": " + str(sean) + "\n"
    fout.write(strout)
fin.close()
fout.close()
