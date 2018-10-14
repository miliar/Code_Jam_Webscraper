def flip(pattern, k):
    ans = ""
    for i in list(pattern)[:k]:
        if i == "+":
            ans += "-"
        else:
            ans += "+"

    ans += pattern[k:]

    return ans
            

def check(pattern, k):
    """if len(pattern)<k or pattern == "".join("+" for i in range(len(pattern))):
        if pattern == "".join("+" for i in range(len(pattern))):
            return 0
        else:
            return -1

    ind = pattern.index("-")
    pattern = pattern[ind:]
    ret = 0
    if(len(pattern)>=k):
        pattern = flip(pattern, k)
        ret += 1
    tmp = check(pattern, k) 
    if tmp != -1:
        return tmp + ret
    else:
        return -1"""
    ans = 0
    while(len(pattern)>0):
        if "-" in pattern:
            ind = pattern.index("-")
            pattern = pattern[ind:]
            if(len(pattern)>=k):
                pattern = flip(pattern, k)
                ans += 1
            else:
                if pattern == "".join("+" for i in range(len(pattern))):
                    return ans
                else:
                    return -1
        else:
            return ans
            

for tc in range(1,int(raw_input())+1):
    pattern,k = raw_input().split()
    k = int(k)
    ans = check(pattern, k)
    if ans == -1:
        ans = "IMPOSSIBLE"
    print "Case #"+str(tc)+": "+str(ans)
