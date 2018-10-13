# python 2.7
# Problem C: Fair and Square - small and large 1

def isPalindrome(x):
    s = str(x)
    return s == s[::-1]

class FairSquare:
    def __init__(self, maxB):
        self.generate(maxB)

    def generate(self, upper):
        self.p = []
        i = 1
        # enough precision for at least 10^14
        limit = int(upper ** .5)
        # generate ordered list, to bisect later
        while i <= limit:
            if isPalindrome(i) and isPalindrome(i * i):
                self.p.append(i * i)
            i += 1

    def count(self, A, B):
        import time
        from bisect import bisect_left, bisect_right

        st = time.time()
        i = bisect_left(self.p, A)
        j = bisect_right(self.p, B)
        return j - i

def answer(case, s):
    return "Case #%d: %s"%(case, s)

if __name__ == "__main__":
    def parse_run(s):
        pairs = [
            map(int, line.split()) for line in s.split("\n")[1:] if line]

        f = FairSquare(max(b for (a,b) in pairs))
        for i, (a,b) in enumerate(pairs):
            print answer(i + 1, f.count(a, b))

    import sys
    try: fn = sys.argv[1]
    except IndexError: fn = "C-large-1.in"

    with file(fn) as fp:
        parse_run(fp.read())

