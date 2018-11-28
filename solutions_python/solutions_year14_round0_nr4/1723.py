def bsearch(mylist, a, left, right):
    if left > right:
        return -1
    if left == right:
        if mylist[left] > a:
            return left
        else:
            return -1

    mid = (left + right) / 2
    if a > mylist[mid]:
        return bsearch(mylist, a, mid + 1, right)
    else:
        return bsearch(mylist, a, left, mid)


def playwar(n, alist, blist):
    left = 0
    right = n - 1
    score = 0
    for i in range(n-1, -1, -1):
        if alist[i] > blist[right]:
            left += 1
            score += 1
        else:
            right -= 1
    return score

def playfake(n, alist, blist):
    score = 0
    aleft = bleft = 0
    aright = bright = n - 1
    for i in range(n):
        if alist[aleft] > blist[bleft]:
            score += 1
            aleft += 1
            bleft += 1
        # elif alist[aright] > blist[bright]:
        #     score += 1
        #     aright -= 1
        #     bleft += 1
        else:
            aleft += 1
            bright -= 1
    return score

if __name__ == "__main__":
    fin = open("D-large.in", "r")
    fout = open("D.out", "w")
    T = int(fin.readline())
    for t in range(T):
        t += 1
        n = int(fin.readline())
        alist = sorted([float(x) for x in fin.readline().strip().split()])
        blist = sorted([float(x) for x in fin.readline().strip().split()])
        print "\t".join([str(x) for x in alist])
        print "\t".join([str(x) for x in blist])
        score1 = playfake(n, alist, blist)
        score2 = playwar(n, alist, blist)
        fout.write("Case #%d: %d %d\n" % (t, score1, score2))
    fout.close()
