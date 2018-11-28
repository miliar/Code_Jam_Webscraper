is_tidy = lambda a:all(a[i] <= a[i+1] for i in xrange(len(a)-1))

def solve(num_str):
    digits = [int(c) for c in num_str]

    while not is_tidy(digits):
        # print digits
        # find first defect
        ndx = 0        
        for i in xrange(len(digits)-1):
            if digits[i]>digits[i+1]:
                ndx=i
                break
        digits[ndx] -= 1
        for i in xrange(ndx+1, len(digits)):
            digits[i] = 9

    # print digits
    n = 0
    for z in digits:
        n = 10*n+z
        
    return n
    
#f = open("e:/work/code_jam/tidy.txt", "r")
f = open("D:/downloads/B-large.in", "r")
T = int(f.readline())
for t in range(T):
    n = f.readline().strip()
    sol = solve(n)
    print "Case #%d: %d"  % (t+1, sol)