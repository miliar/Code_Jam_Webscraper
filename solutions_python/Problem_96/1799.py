# Author: John Duhamel

class player:
    def __init__(self, points):
        # self.p reads "self.p"
        # self.m reads "self.mundane"
        # self.s reads "self.surprising"
        self.p = int(points)

        #handle corner cases first
        if self.p == 0:
            self.m = [0,0,0]
            self.s = [0,0,0]
        elif self.p == 1:
            self.m = [0,0,1]
            self.s = [0,0,1]
        else:
            if self.p % 3 == 0:
                self.m = [self.p/3,   self.p/3, self.p/3]
                self.s = [self.p/3-1, self.p/3, self.p/3+1]
            elif self.p % 3 == 1:
                self.m = [self.p/3,   self.p/3,   self.p/3+1]
                self.s = [self.p/3-1, self.p/3+1, self.p/3+1]
            elif self.p % 3 == 2:
                self.m = [self.p/3, self.p/3+1, self.p/3+1]
                self.s = [self.p/3, self.p/3,   self.p/3+2]
        self.next = None

def dance(j, s, p):
    s = int(s)
    p = int(p)
    d = u = 0

    if j == None:
        if s != 0:
            return -100
        return 0

    if s > 0:
        d = dance(j.next,s-1,p)
        if max(j.s) >= p:
            d += 1

    u = dance(j.next,s,p)
    if max(j.m) >= p:
        u += 1

    return max([d, u])

def solve(l,case):
    l = l.split()
    N, S, p, ti = l[0], l[1], l[2], l[3:]

    players = []
    for j in ti:
        players.append(player(j))

    for j in range(0,len(players)-1):
        players[j].next = players[j+1]

    print "Case #%s: %s" % (case,dance(players[0],S,p))

if __name__=='__main__':
    import sys
    fp = open(sys.argv[1], "r")

    inputs = int(fp.readline())
    for j in range(1, inputs+1):
        solve(fp.readline().strip(), j)

    fp.close()


