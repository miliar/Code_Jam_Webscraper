
def get_res_fast(s):
        pos = 0
        for i in range(len(s)-1):
            if s[i+1] > s[i]:
                pos = i + 1
            elif s[i+1] < s[i]:
                t = str(int(s[pos])-1)
                s = s[:pos] + t + '9'*(len(s)-pos-1) 
                s = str(int(s))
                return s
            else: 
                continue
        return s

t = int(raw_input())  
for i in xrange(1, t + 1):
    x = raw_input().split(" ")[0]
    result = get_res_fast(x)
    print "Case #{}: {}".format(i, result)
