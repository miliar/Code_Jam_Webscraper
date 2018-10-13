def f(s):
    for i in range(len(s)):
        if s[i] < s[max(0, i - 1)]:
            return False
    return True
        
fin = open("B-large.in")
fout = open("output.txt", 'w')


t = int(fin.readline())
for i in range(t):
    s = fin.readline()
    s = [int(j) for j in s[:-1]] + [9]
    for j in range(len(s) - 3, -1, -1):
        if s[j] > s[j + 1]:
            s[j] -= 1
            for w in range(j + 1, len(s)):
                s[w] = 9
    if len(s) > 2:
        q = int('9' * (len(s) - 2))
    else:
        q = 0
    print("Case #", i + 1, ": ", max(q, int(''.join([str(z) for z in s[:-1]]))), sep = "", file = fout)
fout.close()