#https://code.google.com/codejam/contest/2974486/dashboard#s=p3

class Game(object):
    def __init__(self, naomi, ken):
        self.naomi = sorted([float(b) for b in naomi.strip().split()])
        self.ken = sorted([float(b) for b in ken.strip().split()])

    def war(self):
        won = 0
        ken = self.ken[:]
        for n in self.naomi[::-1]:
            kgt = [b for b in ken if b > n]
            if kgt:
                m = min(kgt)
                # print "%f < %f - Ken wins" % (n, m)
            else:
                won += 1
                m = min(ken)
                # print "%f > %f - Naomi wins" % (n, m)
            ken.remove(m)
        return won
        

    def deceit(self):
        won = 0
        ken = self.ken[:]
        for n in self.naomi:
            klt = [b for b in ken if b < n]
            if klt:
                m = min(klt)
                # print "%f > %f - Naomi wins" % (n, m)
                won += 1
            else:
                m = max(ken)
                # print "%f < %f - Ken wins" % (n, m)
        
            ken.remove(m)
        return won
                

if __name__ == '__main__':
    size = 'large'
    fp = open('D-%s.in' % size)
    ap = open('answer-%s.txt' % size, 'w')
    cases = int(fp.readline())

    for i in range(cases):
        blocks = fp.readline()
        game = Game(fp.readline(), fp.readline())
        msg = "Case #%d: %d %d\n" % (i+1, game.deceit(), game.war())
        print msg,
        ap.write(msg)
    fp.close()
    ap.close()
    
