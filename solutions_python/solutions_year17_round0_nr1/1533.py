x = int(input())

for i in range(1,x+1):
    _in = input().strip().split(' ')
    s = list(_in[0])
    size = int(_in[1])

    l = 0
    r = len(s) - 1

    impossible = False

    flips = 0

    pluses = 0
    minuses = 0

    for j in s:
        if j == '+':
            pluses += 1
        else:
            minuses += 1
    
    while (l <= r):
       
        while (l <= r and s[l] == '+'):
            l += 1
            pluses -= 1

        if l > r:
            break;

        if size > r - l + 1:
            impossible = True
            break

        if size == r - l + 1 and pluses != r - l + 1 and minuses != r - l + 1:
            impossible = True
            break

        if s[l] == '-':
            flips += 1
            for j in range(l,l+size):
                if s[j] == '+':
                    s[j] = '-'
                    pluses -= 1
                    minuses += 1
                else:
                    s[j] = '+'
                    pluses += 1
                    minuses -= 1

        while (l <= r and s[r] == '+'):
            r -= 1
            pluses -= 1

        if l > r:
            break;

        if size > r - l + 1:
            impossible = True
            break

        if size == r - l + 1 and pluses != r - l + 1 and minuses != r - l + 1:
            impossible = True
            break

        if s[r] == '-':
            flips += 1
            for j in range(r,r-size,-1):
                if s[j] == '+':
                    s[j] = '-'
                    pluses -= 1
                    minuses += 1
                else:
                    s[j] = '+'
                    pluses += 1
                    minuses -= 1

    if minuses > 0 and pluses > 0:
        impossible = True

    if minuses == r - l + 1 and minuses > 0:
        flips += 1
        
    print("Case #{}: ".format(i),end='')
    if impossible:
        print("IMPOSSIBLE")
    else:
        print(flips)

        
        
