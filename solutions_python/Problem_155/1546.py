def solveA():
    T = input()
    c = 0
    while c < T:
        c += 1
        [s_max, countsStr] = raw_input().split()
        peopleCounts = map(int, countsStr)
        result = "Case #%i: %s" % (c, solve(peopleCounts))
        print result    
def solve(peopleCounts):
    needed = 0
    standing = 0
    for i in range(len(peopleCounts)):
        if standing < i:
            newNeeded = i - standing
            needed += newNeeded
            standing += newNeeded
        standing += peopleCounts[i]
    return needed

solveA()