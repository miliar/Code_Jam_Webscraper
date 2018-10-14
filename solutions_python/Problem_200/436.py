def find(l, n):
    for ind, i in enumerate(l):
        if i == n:
            return ind

t=int(input())
for i in range(1,t+1):
    # print (input().split(' '))
    s=[0]
    inp = input()
    if inp=='0':
        print("Case #{}: {}".format(i,0))
        continue
    s.extend(list(map(int,inp)))
    for p in range(len(s)-1):
        if s[p]>s[p+1]:
            # print (p)
            p = find(s,s[p])
            s[p]-=1
            for q in range(p+1,len(s)):
                s[q]=9
    # s = s[1:] if s[1]!=0 else s[2:]
    for p in range(len(s)):
        if s[p]!=0:
            s = s[p:]
            break

    print("Case #{}: {}".format(i, ''.join(map(str,s))))