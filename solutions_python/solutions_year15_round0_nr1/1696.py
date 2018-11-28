import fileinput


def main():
    t = 1
    for line in fileinput.input():
        if fileinput.isfirstline():
            continue
        mLev, levS = line.split()
        print "Case #{}: {}".format(t, inviteFriends(levS))
        t += 1


def inviteFriends(levS):
    standing = 0
    friends = 0
    for shLev, nb in enumerate(levS):
        if shLev > standing:
            friends += shLev - standing
            standing = shLev
        standing += int(nb)

    return friends


main()
