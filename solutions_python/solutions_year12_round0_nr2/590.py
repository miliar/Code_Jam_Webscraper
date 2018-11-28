debug = False
#debug = True

t = int(raw_input())

for i in range(t):
    row = raw_input()
    row = row.split(" ")
    row.reverse()
    
    n = int(row.pop())
    s = int(row.pop())
    p = int(row.pop())
    
    if debug: print "\n\nn: %d, s: %d, p: %d" %(n,s,p)

    ans = 0

    for j in range(n):
        a = int(row.pop())
        div = a / 3
        mod = a % 3

        if debug: print "t: %d, div: %d, mod: %d (s: %d)" %(a,div,mod,s)

        if mod == 2:
            point = div + 1
        elif mod == 1:
            point = div + 1
        else:
            point = div
        
        if debug and s == 0: print "Empty!!"

        if point >= p:
            if debug: print "pattern: 1"
            ans += 1
        elif s > 0 and mod == 2 and (point + 1) >= p:
            if debug: print "pattern: 2"
            s -= 1
            ans += 1
        elif s > 0 and mod == 0 and (point + 1) >= p and a >= 3:
            if debug: print "pattern: 3"
            s -= 1
            ans += 1
        else:
            if debug: print "pattern: 4"
    
    print "Case #%d: %d" % (i + 1, ans)
