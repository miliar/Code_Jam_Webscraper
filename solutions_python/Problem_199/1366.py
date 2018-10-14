
f = open("1.in")

num_test = int(f.readline())

for iter_test in xrange(num_test):
    line = f.readline()
    s, k = line.split()
    s = list(s)
    k = int(k)
    def flip(c):
        if c == "-":
            return "+"
        else:
            return "-"
    ans = 0 
    for i, c in enumerate(s):
        if i + k > len(s):
            break
        if c == "-":
            for j in xrange(i, i + k):
                s[j] = flip(s[j])
            ans += 1
    
    flag = False
    for j in xrange(i, len(s)):
        if s[j] == "-":
            flag = True

    print "Case #%d:"%(iter_test + 1),
    if flag:
        print "IMPOSSIBLE"
    else:
        print ans
