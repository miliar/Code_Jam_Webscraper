def flip(s, st, k):
    res = s[:st]
    for i in range(st, st + k):
        if (s[i] == '+'):
            res += '-'
        else:
            res += '+'
    res += s[st + k:]
    return res

def solve(s, x):
    t = 0
    x = int(x)
    for i in range(0, len(s) - x + 1):
        if (s[i] == '-'):
            s = flip(s, i, x)
            #print(s)
            t += 1
    for i in range(len(s)):
        if (s[i] == '-'):
            return "IMPOSSIBLE"
    return t   
    

fin = open('input.txt', 'r')
fout = open('output.txt', 'w')

t = int(fin.readline())
for case in range(1, t + 1):
    s, x = fin.readline().strip().split()
    ans = solve(s, x)
    fout.write("Case #" + str(case) + ": " + str(ans) + "\n")

fin.close()
fout.close()