import fileinput


def solve(a1, deck1, a2, deck2):
    cards = set(deck1[a1]) & set(deck2[a2])
    if len(cards) > 1:
        return "Bad magician!"
    if not cards:
        return "Volunteer cheated!"
    return cards.pop()


def main(files=None):
    f = fileinput.input(files)
    readline = lambda: f.readline().strip()

    total = int(readline())
    for i in xrange(total):
        a1 = int(readline()) - 1
        deck1 = [map(int, readline().split()) for _ in xrange(4)]
        a2 = int(readline()) - 1
        deck2 = [map(int, readline().split()) for _ in xrange(4)]

        print "Case #{}: {}".format(
            i + 1,
            solve(a1, deck1, a2, deck2)
        )


main()
