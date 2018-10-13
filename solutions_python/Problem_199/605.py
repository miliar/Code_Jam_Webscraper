
def flip(s, k, i):
    """flipping starting with i's position"""
    rv = s[:i] + s[i:i+k].replace('-', 'm').replace('+', '-').replace('m', '+') + s[i+k:]
    return rv

def solve_simple(s, k):
    flips = 0
    while s.count("+") != len(s):
        pos = s.find("-")
        if pos + k > len(s):
            return "IMPOSSIBLE"
        s = flip(s, k, pos)
        flips += 1
    return flips           

def main():
    t = int(raw_input())
    for i in xrange(1, t + 1):
        raw = raw_input().split(" ")
        s, k = raw[0], int(raw[1])
        rv = solve_simple(s, k)
        print "Case #{}: {}".format(i, rv)
    

if __name__ == "__main__":
    main()
