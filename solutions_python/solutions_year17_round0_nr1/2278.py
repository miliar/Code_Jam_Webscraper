
def flip(new_s,k):
    ans = 0
    n = len(s)
    for j in range(len(s)):
        if(new_s[j] == '-'):
            ans += 1
            if j+k-1 >= n:
                return "IMPOSSIBLE" 
            for l in range(k):
                if(j+l+1 <= len(s) and new_s[j+l] == '-' ):
                    new_s[j+l] = '+'
                elif(j+l+1 <= len(s) and new_s[j+l] == '+'):
                    new_s[j+l] = '-'

    return ans
    
t = int(raw_input().strip())

for i in range(t):
    s,k = raw_input().split()
    new_s = list(s)
    k = int(k)

    print "Case #{}: {}".format(i+1,flip(new_s,k))
