# tidy number is one with digits sorted in non-decreasing order
# want last tidy number before given number

# tidy -> tidy
# 1232 -> 1229 (find first decreasing pair, decrement first digit, fill with 9)
# 12332 -> 12299 (extension)

def solve(n):
    i = 0
    while i + 1 < len(n) and n[i] <= n[i + 1]:
        i += 1
    if i + 1 == len(n):
        return n
    while i > 0 and n[i - 1] == n[i]:
        i -= 1
    result = n[:i] + chr(ord(n[i]) - 1) + '9' * (len(n) - i - 1)
    if len(result) > 1 and result[0] == '0':
        result = result[1:]
    return result

if __name__ == '__main__':
    import sys
    fp = open(sys.argv[1])
    def readline():
        return fp.readline().strip()
    num_cases = int(readline())
    for i in xrange(num_cases):
        n = readline()
        print "Case #%d: %s" % (i + 1, solve(n))
