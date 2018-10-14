def get_ans(s):
    ans = 0
    total = 0
    for i in range(len(s)):
        if total < i:
            ans += i - total
            total = i
        total += int(s[i])
    return ans

T = int(input())
stuff = []

for i in range(T):
    stuff.append(input().split(' ')[1])
for i in range(T):
    print('Case #%d: %d' % (i+1, get_ans(stuff[i])))
