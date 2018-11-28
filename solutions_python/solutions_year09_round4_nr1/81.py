def unordered(a):
    for i in xrange(len(a)):
        if a[i].rfind('1') > i:
            return i
    
if __name__ == "__main__":
    T = int(raw_input())
    for i in xrange(1, T + 1):
        N = int(raw_input())
        a = []
        for x in xrange(N):
            a.append(raw_input())
        
        swaps = 0
        while True:
            x = unordered(a)
            if x == None:
                break
            
            j = x + 1
            while a[j].rfind('1') >= a[x].rfind('1'):
                j += 1
            
            tmp = a[j - 1]
            a[j - 1] = a[j]
            a[j] = tmp
            
            swaps += 1
        
        print "Case #%d: %d" % (i, swaps)

