import sys

numlist = ["ZERO", "TWO", "SIX", "EIGHT", "FOUR", "THREE", "FIVE", "SEVEN", "NINE", "ONE"]

def main(T):
    lines = open(T).read().split('\n')
    N = int(lines[0])
    for i in xrange(1, N+1):
        s = dict((l, lines[i].count(l)) for l in lines[i])
        nums = {"ZERO": 0, "ONE": 1, "TWO":2, "THREE":3, "FOUR":4, "FIVE":5, "SIX":6, "SEVEN":7, "EIGHT":8, "NINE": 9}
        list = sorted([n for n in nums.keys()])
        L = []
        for num in numlist:
            new = True
            while new:
                new = False
                length = len(num)
                count = 0
                for char in num:
                    if char in s and s[char] > 0:
                        count += 1
                if count == length:
                    new = True
                    for char in num:
                        s[char] -= 1
                    L.append(num)

        digits = sorted(str(nums[n]) for n in L)
        print "Case #%d: %s" % (i, "".join(digits))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Arg required"
        sys.exit(1)

    main(sys.argv[1])
