t = input()
for z in xrange(1,t+1):
    c,f,x = map(float,raw_input().split())
    ck = 0.0
    fr = 0
    ans = 0.0
    while x/(2.0+fr*f) > x/(2.0+(fr+1)*f) + c/(2.0+fr*f):
        ans += c/(2.0+fr*f)
        fr += 1
    ans += x/(2.0+fr*f)
    print ("Case #%d: %.7f") % (z,ans)
