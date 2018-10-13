T = input()

def solve1():
    bef = 0
    cnt = 0
    
    rate = 0
    
    for l in ls:
        if l < bef:
            if l < bef:
                cnt += bef - l
                rate = max(rate,bef - l)
        bef = l
    return cnt,rate
    
    
def solve2(rate):
    bef = 0
    cnt = 0
    for l in ls[:-1]:
        if l <= rate:
            cnt += l
        else:
            cnt += rate
    return cnt



for t in range(T):
    N = input()
    ls = map(int,raw_input().split(" "))
    ans1,rate =  solve1()
    ans2 = solve2(rate)
    print "Case #%d: %d %d"%(t+1,ans1,ans2)
    