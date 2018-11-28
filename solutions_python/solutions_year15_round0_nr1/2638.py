
import numpy as np

from profilehooks import profile

def standing_ovation_false(s_max, shyness):
    """
    s_max (int)
    shyness (array of int between 0-9 included)
    """
    assert (s_max >= 0)
    assert (len(shyness) == s_max + 1)

    #print "cumsum: ", shyness.cumsum()
    #print "needs : ", np.arange(0, s_max + 1)

    diff = shyness.cumsum() - np.arange(0, s_max + 1)
    threshold = np.where((diff < 0) & (shyness > 0))[0]

    invites = - diff[threshold].sum()

    return invites

#@profile
def standing_ovation(s_max, crowd):
    """
    s_max (int)
    shyness (array of int between 0-9 included)
    """
    #assert (s_max >= 0)
    #assert (len(crowd) == s_max + 1)

    needs = np.arange(0, s_max + 1)
    invites = 0
    standup = 0

    for need_i in needs:
        if crowd[need_i] > 0:
            new_invites = (need_i - standup) if need_i > standup else 0
            invites += new_invites
            standup += crowd[need_i] + new_invites

    return invites



def tc():
    T = int(raw_input())

    for t in range(T):
        s_max, crowd = raw_input().split()
        s_max = int(s_max)
        crowd = np.array( map(int, list(crowd.strip())) )
        #print "#", t, s_max, shyness
        invites = standing_ovation(s_max, crowd)
        print "Case #%d: %d" % (t + 1, invites)

if __name__ == '__main__':
    tc()
