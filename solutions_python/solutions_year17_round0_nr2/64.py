import sys

def find_violation(s):
    """Finds the first position of a digit that is smaller than its predecessor. None if not found."""
    for i in range(1, len(s)):
        if s[i] < s[i-1]:
            return i
    return None

def largest_tidy(N):
    """returns a string."""
    s = str(N)
    while True:
        pos = find_violation(s)
        if pos is None:
            return s
        lens = len(s)
        s = s[:pos] + ('0' * (lens-pos))
        assert len(s) == lens
        n = int(s) - 1
        s = str(n)

if __name__ == "__main__":
    ncases = int(sys.stdin.readline().strip())
    for i in range(ncases):
        N = int(sys.stdin.readline())
        print "Case #%d: %s" % (i+1, largest_tidy(N))
