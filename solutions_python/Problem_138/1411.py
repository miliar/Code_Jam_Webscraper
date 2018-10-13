"""
Deceitful War

See: https://code.google.com/codejam/contest/2974486/dashboard#s=p3

"Knowledge is Power"

We can assert that the player that has more knowledge can take as much points
as long he does not need to bend math rules.

`war()` returns the minimal number of points a player must win, even if he
chooses the worst outcome.  This means the other player throws the lowest
block he can at any turn, winning or losing.

In a Deceitful War, the table turns.

"""

from bisect import bisect_right
import fileinput


def war(my, his):
    """
    Returns the number of items that a better player just cant take from me.
    """
    my, his = sorted(my), sorted(his)
    points = 0
    while my:
        x = my.pop(0)
        if x > his[-1]:
            his.pop(0)
            points += 1
        else:
            his.pop(bisect_right(his, x))
    return points


def main(files=None):
    f = fileinput.input(files)
    readline = lambda: f.readline().strip()

    total = int(readline())
    for i in xrange(total):
        blocks = int(readline())
        naomi = map(float, readline().split())
        ken = map(float, readline().split())
        print "Case #{}: {} {}".format(
            i + 1,
            blocks - war(ken, naomi),
            war(naomi, ken)
        )


main()
