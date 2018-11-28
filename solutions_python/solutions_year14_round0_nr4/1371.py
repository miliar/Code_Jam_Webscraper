def War(N, Naomi, Ken):
    count = 0
    f = 0
    for i in xrange(N):
        if Naomi[i] > Ken[f]:
            count += 1
        else:
            f += 1
    return count

def Deceitful(N, Naomi, Ken):
    count = 0
    for i in xrange(N):
        if Naomi[0] > Ken[0]:
            Naomi.pop(0)
            Ken.pop(0)
            count += 1
        else:
            Naomi.pop()
            Ken.pop(0)
    return count

def RunTest(N, Naomi, Ken):
    W = War(N, Naomi, Ken)
    D = Deceitful(N, Naomi, Ken)
    return D, W

def main():
    numTests = int(raw_input())
    for i in xrange(numTests):
        N = int(raw_input())
        Naomi = sorted([float(c) for c in raw_input().split()], reverse=True)
        Ken = sorted([float(c) for c in raw_input().split()], reverse=True)
        D, W = RunTest(N, Naomi, Ken)
        print "Case #" + str(i + 1) + ": " + str(D) + " " + str(W)

main()
