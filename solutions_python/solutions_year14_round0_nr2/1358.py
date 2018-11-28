from sys import stdin

def handleTest(case, line):
    # Default rate is 2 cps
    # Need C cookies to buy a farm
    # Farm costs C cookies
    # Afterward you get F extra cookies per second
    # Need X cookies to win
    C, F, X = map(float, line.split(" "))
    rate = 2.0  # Default rate

    # print "                   C:", C, ", F:", F, ", X:", X

    div = X / C

    if div < 1.0:
        timeToWin = X / rate
        # Done after a single second
        print "Case #%s: %s" % (case, timeToWin)
        return

    numSeconds = 0
    while True: 
        secondsTillWin = X / rate  # seconds to win now
        secondsTillFarm = C / rate  # seconds to buy a farm now
        secondsToWinAfterFarm = X / (rate + F)  # seconds to win post farm buy

        secondsToWinWithFarm = secondsTillFarm + secondsToWinAfterFarm

        if secondsTillWin > secondsToWinWithFarm:
            # better to buy a farm
            rate += F
            numSeconds += secondsTillFarm

            # print "    bought a farm, newRate:", rate, ",", secondsTillFarm
            # print "                       time to win:", secondsTillWin
            # print "                              time:", numSeconds
        else:
            # print "    done:", secondsTillWin

            # Done
            numSeconds += secondsTillWin
            break

    print "Case #%s: %s" % (case, numSeconds)


if __name__ == '__main__':
    data = stdin.read().strip()

    lines = data.split("\n")

    numTests = int(lines[0])

    case = 1
    for line in lines[1:]:
        handleTest(case, line)
        case += 1
