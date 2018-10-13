
for tc in range(1, int(raw_input())+1):
    name, n = raw_input().split()
    cons = 0
    pos = []
    for i in range(len(name)):
        if not name[i] in ['a', 'i', 'e', 'o', 'u']:
            cons += 1
            if cons >= int(n):
                pos.append(i)
        else:
            cons = 0
    res = 0
    for i in range(len(name)):
        for j in pos:
            if j >= i + int(n)-1:
                res += len(name) - j 
                break

    print("Case #"+str(tc)+": "+str(res))
