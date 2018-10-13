import random

def war(Niaomi, Ken):
    Niaomi_war = Niaomi[:]
    Ken_war = Ken[:]
    p = 0
    while len(Niaomi_war) != 0:
        n = random.randint(0, len(Niaomi_war)-1)
        if Niaomi_war[n] > Ken_war[-1]:
            p += 1
            Ken_war.pop(0)
        else:
            for k in xrange(len(Ken_war)):
                if Ken_war[k] > Niaomi_war[n]:
                    Ken_war.pop(k)
                    break
        Niaomi_war.pop(n)

    return p

def war_quick(Niaomi, Ken):
    Niaomi_war = Niaomi[:]
    Ken_war = Ken[:]
    p = 0
    for n in xrange(len(Niaomi_war)):
        if Niaomi_war[n] > Ken_war[-1]:
            p += 1
            Ken_war.pop(0)
        else:
            for k in xrange(len(Ken_war)):
                if Ken_war[k] > Niaomi_war[n]:
                    Ken_war.pop(k)
                    break

    return p


if __name__ == '__main__':
    T = int(raw_input())

    for i in xrange(T):
        N = int(raw_input())
        Niaomi = sorted(map(float, raw_input().split()))
        Ken = sorted(map(float, raw_input().split()))

        war_points = war_quick(Niaomi, Ken)
        decitful_war_points = N - war_quick(Ken, Niaomi)

        print 'Case #%d: %d %d' %(i+1, decitful_war_points, war_points)

