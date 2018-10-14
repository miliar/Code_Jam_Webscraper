# python 2.7

import os, sys

class Input:
    def __init__(self, fp): self.fp = fp
    def m(self, n, t=str):  return [map(t, list(self.line())) for i in range(n)]
    def ms(self, n, t=str, sep=' '):  return [map(t, self.line().split(sep)) for i in range(n)]
    def line(self):  return self.fp.readline().strip()
    def words(self): return self.line().split()
    def int(self):   return int(self.line())
    def ints(self):  return map(int, self.words())
    def float(self): return float(self.line())
    def floats(self):return map(float, self.words())
    def str(self):   return self.line()
    def types(self, *types): return [t(w) for t,w in zip(types, self.words())]

if __name__ == "__main__":
    fn = "test.txt" if len(sys.argv) <= 1 else sys.argv[1]
    f = Input(open(fn))
    fout = open(os.path.splitext(fn)[0] + ".out", "w")

    def answer(t, ans):
        o = "Case #%d: %s\n"%(t, ans)
        sys.stdout.write(o)
        fout.write(o)

    for tc in range(f.int()):
        FarmCost, FarmOutput, X = f.floats()
        #if tc != 3: continue
        FarmRecoupTime = FarmCost / FarmOutput

        c = 0.
        t = 0
        p = 2.
        while 1:
            # time before we can afford anything is uninteresting
            goaltime = (X - c) / p
            farmtime = (FarmCost - c) / p
            jumptime = min(goaltime, farmtime)
            t += jumptime
            #c += jumptime * p

            #print goaltime, farmtime

            if goaltime <= farmtime:
              #  print "I reached the goal in t=%s"%t
                break
            #else:
             #   print "In %.2f seconds (%.2f more), I have %d cookies (p = %d)!"%(t, jumptime, c, p)

            #print "\ng, f, r, ", goaltime, farmtime, FarmRecoupTime

            if FarmRecoupTime + farmtime < goaltime:
                #c -= FarmCost
                p += FarmOutput
            else:

                t += goaltime - jumptime
                break

        answer(tc + 1, t)
