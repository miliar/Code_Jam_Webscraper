import operator

def isEven(num):
    return num % 2 == 0


# Main
t = int(raw_input())

for x in xrange(1, t+1):
    N, people = map(int, raw_input().split())

    if N == people:
        print "Case #{}: {} {}".format(x, 0, 0)
        continue


    emptyStalls = [[N]]

    for p in xrange(0, people):
        emptyStalls = sorted(emptyStalls, key=operator.itemgetter(0), reverse=True)

        bestStall = emptyStalls[0]
        available = bestStall[0]

        if isEven(available):
            left  = (available/2) - 1
            right = (available/2)
        else:
            left  = (available-1) / 2
            right = (available-1) / 2


        # Last person to choose
        if p+1 == people:
            print "Case #{}: {} {}".format(x, max(left, right), min(left, right))
            continue


        emptyStalls = [[left]] + [[right]] + emptyStalls[1:]
