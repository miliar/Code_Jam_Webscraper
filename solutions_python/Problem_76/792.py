import sys, math
from multiprocessing import Pool

def main(data):
    N, candies = data
    if reduce(lambda a,b: a^b, candies) != 0:
        return "NO"
    else:
        return sum(candies) - min(candies)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        f = open(sys.argv[1])
    else:
        f = open("test.txt")
    T = int(f.readline())
    data = []
    for i in range(T):
        N = int(f.readline())
        candies = map(int, f.readline().split())
        data.append((N, candies))
    
#    pool = Pool()
#    r = pool.map(main, data)
    r = map(main, data)
    for i in range(T):
        print "Case #%d: %s" % (i+1, r[i]) 