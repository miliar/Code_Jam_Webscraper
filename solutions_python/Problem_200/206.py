def tidy(s):
    for i in range(len(s)-1):
        if s[i] > s[i+1]:
            return False
    return True

def lastidy(s):
    if tidy(s) == True:
        return int(s)
    L1change = True
    L1 = -1 # last increasing index
    for i in range(len(s)-1):
        if s[i] < s[i+1] and L1change:
            L1 = i
        if s[i] > s[i+1]:
            L1change = False
    res = s[:L1+1] + str(int(s[L1+1])-1) + '9'*(len(s)-L1-2)
    return int(res)

for T in range(int(input())):
    res = lastidy(input())
    print("Case #%d: %d"%(T+1,res))
