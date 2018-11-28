import sys, StringIO

class Harmony(object):
    def __init__(self, n, l, h, p):
        self.l = l
        self.h = h
        self.p = p

    def run(self):
        for i in range(l, h+1):
            ok = True
            for p in self.p:
                #print "Test %d %% %d and %d %% %d" % (i,p,p,i)
                ok = ok and (i%p==0 or p%i==0)
                if not ok: break
            if ok: return i
        return "NO"
    #run

if __name__=="__main__":
    fp = StringIO.StringIO("""2
3 2 100
3 5 7
4 8 16
1 20 5 2""")
    fp = sys.stdin
    for case in range(int(fp.readline())):
        n, l, h = map(int, fp.readline().strip().split())
        p = map(int, fp.readline().strip().split())

        game = Harmony(n, l, h, p)
        print "Case #%d: %s" % (case+1, game.run())
