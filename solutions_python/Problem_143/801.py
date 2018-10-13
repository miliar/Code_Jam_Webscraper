def main():
    testCases = int(raw_input())
    for i in xrange(testCases):
        parts = [int(x) for x in raw_input().split(" ")]
        res = testCase(parts)
        print "Case #%d:" % (i + 1),
        print res
            

def testCase(parts):
    a = parts[0]
    b = parts[1]
    k = parts[2]
    
    res = 0
    for i in xrange(a):
        for j in xrange(b):
            if (i) & (j) < k:
                res += 1
                
    return res

if __name__ == "__main__":
    main()