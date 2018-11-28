

def solve(s, k):
    ret = 0
    cnt = 0
    f = [0 for i in xrange(len(s))]

    # The goal is to get all 1
    for i in xrange(len(s)-k+1):
        if (s[i] + cnt) % 2 == 0:
            # Flip it
            f[i] = 1
            ret += 1
        cnt += f[i]
        if (i-k+1) >= 0:
            cnt -= f[i-k+1]

    # Check the remaining part
    for i in xrange(len(s)-k+1, len(s)):
        if (s[i] + cnt) % 2 == 0:
            # Fail
            return "IMPOSSIBLE"
        if (i-k+1) >= 0:
            cnt -= f[i-k+1]
    
    return ret


n = int(raw_input())
for i in xrange(n):
    s, k = raw_input().split(" ")
    st = []
    
    # transform to 0,1
    for ch in s:
        if ch == "-": st.append(0)
        else: st.append(1)

    print "Case #{}: {}".format(i+1, solve(st, int(k)))