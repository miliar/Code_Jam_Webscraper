
def cal(s,k):
    display = '0' + str(len(s))+'b'
    count = 0
    for i in range(len(s)):
        if s[i] == '1':
            continue
        if len(s) - i < k:
            return "IMPOSSIBLE"
        temp = int(s[i:],2)
        mask = pow(2,len(s)-i-k) - 1
        ori = temp & mask
        temp = temp | mask
        mask = pow(2,len(s)-i) - 1
        temp = temp ^ mask
        temp = temp + ori
        s = format(temp,display)
        count = count + 1
    return count

t = int(raw_input())

for i in range(t):
    s,k = raw_input().split(" ")
    s = s.replace('-','0')
    s = s.replace('+','1')
    result = cal(s,int(k))
    print("Case #{}: {}".format(i+1,result))