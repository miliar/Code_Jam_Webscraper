import sys, math
def isFairAndSquare(n):
    sq = math.sqrt(n)
    return (n == int(str(n)[::-1])) and (sq == float(str(int(sq))[::-1]))
    
def calc(l, h):
    s = 0
    for i in range(l, h + 1):
        if isFairAndSquare(i):
            s += 1
    return s
    
def main():
    f = open(sys.argv[1])
    for i in range(1, int(f.readline()) + 1):
        n = f.readline().split()
        print "Case #" + str(i) + ":", calc(int(n[0]), int(n[1]))
    f.close()
    
if __name__=="__main__":
    main()
