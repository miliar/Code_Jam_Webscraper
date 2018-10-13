import sys

name = "A-large"
path = ""

sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")

testCases = int(input())

def flip(s, start, end):
    l = list(s)
    for i in xrange(start, end):
        if l[i] == '-':
            l[i] = '+'
        else:
            l[i] = '-'
    return ''.join(l)
    
def turn(s, k):
    count = 0
    start = 0
    end   = len(s) - k + 1
    while start < end:
        if s[start] == '-':
            s = flip(s, start, start+k)
            count += 1
        else:
            start += 1
    if '-' in s:
        return "IMPOSSIBLE"
    return count

for testCase in range(1, testCases + 1):
    line = raw_input().split()
    s = line[0]
    k = int(line[1])
    
    res = turn(s, k)

    print("Case #" + str(testCase) + ": " + ("%s" % str(res)))