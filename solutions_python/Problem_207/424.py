fin = open("B-small-attempt1.in")
fout = open("output.txt", "w")

t = int(fin.readline())
for q in range(t):
    n, r, o, y, g, b, v = map(int, fin.readline().split())
    print("Case #", q + 1, ": ", sep = '', file = fout, end = "")
    if r > b + y or b > r + y or y > b + r:
        print("IMPOSSIBLE", file = fout)
    else:
        s = ' '
        for i in range(n):
            if max(r, b, y) == r and s[-1] != 'R' and r > 0:
                s += 'R'
                r -= 1
            elif (max(r, b, y) == b or max(r, b, y) == r) and s[-1] != 'B' and b > 0:
                s += 'B'
                b -= 1
            elif s[-1] != 'Y' and y > 0:
                s += 'Y'
                y -= 1
            elif r > b or s[-1] == 'B':
                s += 'R'
                r -= 1
            else:
                s += 'B'
                b -= 1
        if len(s) != 2 and s[-1] == s[1]:
            s = list(s)
            for i in range(-2, -n, -1):
                if s[i] != s[-1] and (i == -2 or s[i + 1] != s[-1]) and s[i - 1] != s[-1]:
                    s[i], s[-1] = s[-1], s[i]
                    break
            s = ''.join(s)
        print(s[1:], file = fout)
        
fout.close()