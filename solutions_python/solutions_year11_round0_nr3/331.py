import sys

def split(candies):
    assert len(candies) > 0
    amin = candies[0]
    sumSean = 0
    sumPatrick = 0
    for c in candies:
        sumSean += c
        sumPatrick ^= c
        if amin > c:
            amin = c
    if sumPatrick != 0:
        return None
    return sumSean - amin

def main():
    f = open(sys.argv[1])
    T = int(f.readline())
    
    for t in range(1, T+1):
        f.readline() # ignoring
        candies = [int(c) for c in f.readline().split()]
        asum = split(candies)
        if asum is None:
            print "Case #%d: NO" % t
        else:
            print "Case #%d: %d" % (t, asum)

if __name__ == "__main__":
    main()