

import sys

class bt:
    def __init__(self,l):
        
        self.prob = float(l[0])
        self.kw = ""
        try:
            x = float(l[1])
        except ValueError:
            self.kw = str(l[1])
            self.A = bt(l[2:])
            l = self.A.rest()
            self.B = bt(l)
            l = self.B.rest()
            self.r = l
        except IndexError:
            self.r = []
        else :
            self.r = l[1:]

    def rest(self):
        return self.r

    def follow(self,w,p):
        if self.kw =="":
            
            return self.prob * p
        else:
            if self.kw in w:
                return self.A.follow(w,self.prob * p)
            else:
                return self.B.follow(w,self.prob * p)


with open(sys.argv[1]) as f:
    for n in range(int(f.readline())):
        s = ""
        for L in range(int(f.readline())):
            s += f.readline().strip()
            s = " ".join(s.split(")"))
            s = " ".join(s.split("("))
        l = s.split()
        b = bt(l)
        print("Case #",str(n+1),":",sep="")
        for m in range(int(f.readline())):
            w = f.readline().split()[2:]
            prob = b.follow(w,1.0)
            print("{0:.6f}".format(prob))
