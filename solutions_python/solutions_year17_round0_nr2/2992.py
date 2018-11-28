f = open('ans.txt', 'w')
t = int(input())
for h in range(1, t+1):
    s = input()
    if int(s) < int("1"*len(s)):
        f.write(f"Case #{h}: "+"9"*(len(s)-1)+"\n")
    else:
        n = [int(i) for i in s]
        ans = [0]
        for i in range(len(s)):
            if n[i] < ans[i]:
                ans[i] -=1
                for l in range(len(s)-i):
                    ans.append(9)
                while ans[i] < ans[i-1]:
                    ans[i] = 9
                    i-=1
                    ans[i]-=1
                break
            ans.append(n[i])
        y = ''.join([str(i) for i in ans[1:]])
        f.write(f"Case #{h}: {y}\n")
f.close()
