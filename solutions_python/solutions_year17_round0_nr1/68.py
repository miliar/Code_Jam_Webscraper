
def f(s, k):
    fs = []
    cnt = 0

    for i in range(len(s)):
        c = s[i]

        if (len(fs) > 0 and fs[0] == i):
            fs.pop(0)            

        revStat = len(fs)%2
        if c == '-' and not revStat or c == '+' and revStat:
            if i + k - 1 >= len(s):
                return 'IMPOSSIBLE'

            cnt += 1
            fs.append(i+k)

    return cnt

t = int(input())
for i in range(t):
    s, k = input().split()
    print('Case #' + str(i+1) + ':', f(s, int(k)))
    
