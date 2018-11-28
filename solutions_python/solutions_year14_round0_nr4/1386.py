t = int(raw_input())
case = 1
while t > 0:
    t -= 1
    n = int(raw_input())
    a = map(float, raw_input().split())
    b = map(float, raw_input().split())
    a.sort()
    b.sort()
    l, r = 0, n-1
    index = n-1
    ans = 0
    while index >=0:
        num = a[index]
        if b[r] > num:
            r -= 1
            index -= 1
        else:
            l += 1
            index -= 1
            ans += 1

    ans2 = 0
    al, ar = 0, n-1
    bl, br = 0, n-1
    while al <= ar:
        #print al, ar, bl, br
        if b[br] > a[ar]:
            al += 1
            br -= 1
        else:
            ar -= 1
            br -= 1
            ans2 += 1

    print "Case #%s: %s %s" % (case, ans2, ans)
    case += 1


