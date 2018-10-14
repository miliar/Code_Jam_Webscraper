
import sys
import bisect

def deceitful_war_score(naomi, ken):
    """
    Returns Naomi's score if she plays Deceitful War optimally
    against Ken.
    """

    # Suppose that Naomi always calls out 0.99999...
    # then Ken will play his smallest block each time
    # Naomi can then choose (as Ken had done in regular War)
    # to play her minimum such block that is greater than
    # Ken's chosen block

    # However, if her largest block is smaller than Ken's
    # smallest block, then she must revert back to regular
    # War, and will play truthful

    naomi = sorted(naomi)
    ken = sorted(ken)
    length = len(ken)

    score = 0

    while length > 0:
        if naomi[-1] > ken[0]:
            # Play deceitfully
            kblock = ken.pop(0)     # Ken plays his smallest block
            i = bisect.bisect_left(naomi, kblock)
            assert i < length       # Naomi still has something greater
            naomi.pop(i)
            score += 1

        else:
            # Play truthfully (taken from war_score() function)
            nblock = naomi.pop(0)   # Naomi plays her smallest block
            i = bisect.bisect_left(ken, nblock)
            if i == length:
                score += 1
                ken.pop(0)
            else:
                ken.pop(i)

        length -= 1

    return score

def war_score(naomi, ken):
    """
    Returns Naomi's score if she plays War optimally
    against Ken.
    """

    # Ken will play the minimum such block that is greater than
    # Naomi's chosen block, or his smallest if he has none greater

    ken = sorted(ken)
    length = len(ken)

    score  = 0

    for nblock in naomi:
        i = bisect.bisect_left(ken, nblock)
        if i == length:
            score += 1
            ken.pop(0)
        else:
            ken.pop(i)
        length -= 1

    return score


if __name__ == '__main__':

    num_cases = int(sys.stdin.readline())

    for i in xrange(1, num_cases + 1):
        sys.stdin.readline()        # ignore number of masses
        naomi = [float(x) for x in sys.stdin.readline().split()]
        ken = [float(x) for x in sys.stdin.readline().split()]

        dw_score = deceitful_war_score(naomi, ken)
        w_score = war_score(naomi, ken)

        print 'Case #%d: %d %d' % (i, dw_score, w_score)
