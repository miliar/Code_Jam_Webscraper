N = 1
l = []

def doit2():
    global N
    global l
    m = 0
    for i in range(0, len(l)-1):
        if(l[i+1] - l[i] > m):
            m = l[i+1] - l[i]
    ans = 0
    for i in range(0, len(l)-1):
        if(l[i] <= m):
            ans += l[i+1]
        else:
            ans += m
    return ans
