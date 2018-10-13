def is_tidy(n):
    s = str(n)
    for i in range(len(s)-1):
        if int(s[i]) > int(s[i+1]): return False
    return True

for case in range(1,1+int(raw_input())):
    n = int(raw_input())
    for i in range(-1, -len(str(n)), -1):
        if is_tidy(n): break
        if -i >= len(str(n)): break
        n -= (int(str(n)[i])+1) * 10**(-i-1)
    print "Case #%d: %d" % (case, n)
