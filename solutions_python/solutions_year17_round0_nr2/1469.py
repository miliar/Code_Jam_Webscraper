#!/usr/bin/python3
last = "0"
T = int(input())
for t in range(T):
    s = input()
    #s = str(t+1)
    '''
    ok = True
    for i in range(1, len(s)):
        if s[i]<s[i-1]:
            ok = False
    if ok:
        last = s
    '''
    ans = list(s)
    for i in range(1, len(ans)):
        if ans[i] < ans[i-1]:
            j = i-1
            while (j > 0) and (ans[j-1] == ans[j]):
                j -= 1
            ans[j] = chr(ord(ans[j])-1)
            for k in range(j+1, len(ans)):
                ans[k] = '9'
    while ans[0] == '0':
        ans.pop(0)
    ans = ''.join(ans)
    print("Case #{}: {}".format(t+1, ans))
    '''
    if ans != last:
        print("Fail! ", s, ans, last)
        break
    '''
