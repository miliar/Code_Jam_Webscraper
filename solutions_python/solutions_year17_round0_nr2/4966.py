def isTidy(num):
    digits = list(str(num))
    for i in range(len(digits)-1):
        if digits[i+1] < digits[i]:
            return False;
    return True

def previousTidy(N):
    while N >= 0:
        if isTidy(N):
            return N
        N -= 1
    return 0

cases = int(raw_input())
#print "processing", cases, "cases..."
for case in xrange(1, cases+1):
    #print case, "/", "cases"
    N = int(raw_input())
    print "Case #{}: {}".format(case, previousTidy(N))