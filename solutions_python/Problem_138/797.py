from sys import stdin as fp

def war(Na, Ke):
    Ke = sorted(Ke)
    Na_wins = 0
    for Na_card in Na:
        Ken_card = Ke[0]
        for i, Ke_card_cur in enumerate(Ke):
            if Ke_card_cur > Na_card:
                Ken_card = Ke.pop(i)
                break
        if Na_card > Ken_card:
            Na_wins += 1
    return Na_wins


def deceitful_war(Na, Ke):
    Na = sorted(Na)
    Ke = sorted(Ke)
    Na_wins = 0
    for i in range(len(Na)):
        if Na[0] < Ke[0]:
            Na.pop(0)
            Ke.pop(-1)
        else:
            Na.pop(0)
            Ke.pop(0)
            Na_wins += 1
    return Na_wins
                    
            

T = int(fp.readline())
for i in xrange(T):
    N = int(fp.readline())
    Na = sorted(map(float, fp.readline().split()))
    Ke = sorted(map(float, fp.readline().split()))
    print "Case #%s: %s %s" % (i+1, deceitful_war(Na, Ke), war(Na, Ke))    
