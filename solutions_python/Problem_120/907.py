import math
def calc(r, t):
    n = (-2*r + int(math.sqrt(4*r**2 + 8*t)))//4 + 2
    while True:
        now = 2*n*n+ 2*r*n - n;
        if now <= t:
            return n
        n -= 1
    

def main():
    fin = open("A-small-attempt0.in", "r")
    fout = open("bullsey.out", "w")
    T= int(fin.readline())
    for i in xrange(T):
        s = fin.readline().split()
        r = int(s[0])
        t = int(s[1])
        fout.write("Case #%d: %d\n" %(i+1, calc(r, t)))

if __name__ == '__main__':
    main()
