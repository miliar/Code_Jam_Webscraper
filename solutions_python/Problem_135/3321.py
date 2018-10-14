def read(n):
    ans = []
    for i in xrange(0,4):
       temp = raw_input().split()
       if i == n-1:
        ans = [int(e) for e in temp]
    return ans

def check(ans1, ans2):
    res = []
    for e in ans1:
        if e in ans2:
            res += [e]
    if len(res) == 0:
        return "Volunteer cheated!"
    elif len(res) == 1:
        return res[0]
    else:
        return "Bad magician!"
# Main
t = int(raw_input())

for i in xrange(0,t):
    a1 = int(raw_input())
    ans1 = read(a1)
    a2 = int(raw_input())
    ans2 = read(a2)
    
    print "Case #%d:" % (i+1), check(ans1,ans2)
  
