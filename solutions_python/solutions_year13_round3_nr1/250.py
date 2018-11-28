cons = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

def f(s, n):
    ans = 0
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            cs = s[i:j]
            #print(cs)
            flag = 0
            for q in range(len(cs) - n + 1):
                flag1 = 1
                for w in range(q, q + n):
                    #print(q, w)
                    if not cs[w] in cons:
                        flag1 = 0
                if flag1 == 1:
                    flag = 1
            ans += flag
    print(ans)
                

quant = int(input())
for qw in range(quant):
    print('Case #' + str(qw + 1) + ': ', end = '')
    a = input().split()
    f(a[0], int(a[1]))
