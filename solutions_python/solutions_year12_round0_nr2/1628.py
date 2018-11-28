
def categorise (total, best):
    avg = total // 3
    # best, best-1, best-1
    lowestNoSurprise = best + 2*max(0,best-1)
    # best, best-2, best-2
    lowestSurprise = best + 2*max(0, best-2)
    if total >= lowestNoSurprise:
        return (0, 1)
    if total >= lowestSurprise:
        return (1, 0)
    return (0, 0)

def solve (surprises, best, totals):
    noSurprise, surprise = (0,0)
    for total in totals:
        a, b = categorise (total, best)
        # print (total, best, a, b)
        surprise += a
        noSurprise += b
    maxBest = noSurprise + min(surprise, surprises)
    return maxBest

def go (fNameIn, fNameOut):
    inF = open (fNameIn, 'r')
    outF = open (fNameOut, 'w')
    lines = inF.readlines()[1:]
    count = 1
    for l in lines:
        out = "Case #" + str(count) + ": " + str(processLine (l)) + "\n"
        print (out)
        outF.write(out)
        count += 1
    inF.close()
    outF.close()

def processLine (l):
    ll = l.split()
    (n, s, p, *t) = ll
    ans = solve (int(s), int(p), [int(i) for i in t])
    return ans

if __name__ == "__main__":
    # processFile ('in.txt', 'out.txt')
    pass

