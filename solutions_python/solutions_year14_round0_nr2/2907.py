
def game(c,f,x):
    cookies = 2
    farm_pre = 0
    farm_new = (c/cookies)
    while (x/cookies + farm_pre > (farm_new + x/(cookies+f))):
        cookies += f
        farm_pre = farm_new
        farm_new += c/cookies
    return farm_pre + x/(cookies)



n = int(raw_input())
for case in range(1, n+1):
    c, f, x = map(float,raw_input().split())
    print "Case #%d: %.7f" %(case,game(c,f,x))

