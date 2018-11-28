import sys

def howLongToHitTarget(production, target):

    return target / production

def howLongToBuyFarm(production, cost):

    return cost / production

def main(lines):

    ncases = int(lines.pop(0))

    for case in xrange(ncases):
        production = 2
        seconds = 0.0

        cost, factor, target = lines.pop(0).split()
        cost = float(cost)
        factor = float(factor)
        target = float(target)

        curr = 0.0
        next = 0.0
        while True:
            curr = target / production + seconds
            next = cost / production + target / (production + factor) + seconds
            
            if curr < next:
                print 'Case #%d: %0.7f' % (case + 1, curr)
                break

            seconds += cost / production
            production += factor

if __name__ == '__main__':
    main(sys.stdin.readlines())
