import sys


class Prob(object):
    def __init__(self, naomi, ken):
        self.naomi = naomi
        self.ken = ken

    def solve(self):
        # results
        points_naomi, points_naomi_deceitful = 0, 0
        strategy1, strategy2 = 0, 0
        # legar war
        naomi = self.naomi[:]
        ken = sorted(self.ken[:])

        for t in naomi:
            for k in xrange(len(ken)):
                if ken[k] > t:
                    k_play = k
                    break

            else:
                k_play = 0
                points_naomi += 1

            ken.pop(k_play)

        #if counter == 3:
        #    import ipdb; ipdb.set_trace() # BREAKPOINT
        # deceitful war
        naomi = sorted(self.naomi[:])
        ken = sorted(self.ken[:])
        for t in xrange(len(naomi)):
            if naomi[0] > ken[-1]:
                break
            else:
                naomi.pop(0)
                ken.pop()

        strategy1 = len(naomi)

        naomi = sorted(self.naomi[:])
        ken = sorted(self.ken[:])
        for t in xrange(len(naomi)):
            for k in xrange(len(ken)):
                if naomi[t] > ken[k]:
                    blaff_ken = k
                    break
            else:
                continue

            strategy2 += 1
            ken.pop(blaff_ken)

        points_naomi_deceitful = max(strategy1, strategy2)

        return "%d %d" % (points_naomi_deceitful, points_naomi)

output = "Case #%d: %s"

with open(sys.argv[1], 'r') as f:
    T = int(f.readline())
    for counter in xrange(T):
        n = f.readline()
        naomi = [float(i) for i in f.readline().split()]
        ken = [float(i) for i in f.readline().split()]

        p1 = Prob(naomi, ken)
        print output % (counter+1, p1.solve())
