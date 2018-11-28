fp = open("C-large.in")
def get():
    return fp.readline().strip()

def solve(n, c):
    assert len(c) == n
    if reduce(lambda x,y: x ^ y, c):
        return "NO"
    else:
        return sum(c) - min(c)
    
def main():
    nc = int(get())
    for i in xrange(nc):
        ans = solve(int(get()), map(int, get().split()))
        print "Case #%d: %s" % (i+1, ans)

if __name__ == "__main__":
    main()