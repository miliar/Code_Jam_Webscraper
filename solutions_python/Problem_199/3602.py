f1 = open("A/A-small-attempt1.in", "r")
t = int(f1.readline().split('\n')[0])
for i in range(t):
    x = f1.readline().split('\n')[0]
    k = int(x.split(' ')[1])
    s = list(x.split(' ')[0])
    len_s = len(s)
    happy = s.count('+')
    if happy == len_s:
        flips = 0
    else:
        flips = 0
        j = 0
        while len_s - j >= k:
            if s[j] == '-':
                for c in range(j, j+k):
                    if s[c] == '-':
                        s[c] = '+'
                    else:
                        s[c] = '-'
                flips += 1
            j += 1
    f2 = open("A/output.txt", "a")
    if '-' in s:
        f2.write("Case #"+str(i+1)+": IMPOSSIBLE")
    else:
        f2.write("Case #"+str(i+1)+": "+str(flips))
    f2.write("\n")
    f2.close()
