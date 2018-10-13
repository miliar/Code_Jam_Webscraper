ret = []
with open('A-large.in', 'r') as file:
    t = int(file.readline())
    for __ in range(t):
        s, k = file.readline().split()
        k = int(k)
        a = [0 if x == '+' else 1 for x in s]

        # it doesn't matter what order you make your flips, so the brute-force approach is 2**(len(a)-k)
        # a small step further and we see that it's len(a)*k time if we scan in one direction, enough to solve large
        flips = 0
        for i in range(len(a)-k+1):
            if a[i]:
                flips += 1
                for j in range(i, i+k):
                    a[j] ^= 1
        if sum(a) == 0:
            ret.append(flips)
        else:
            ret.append(-1)

with open('Aout_large.txt', 'w') as outfile:
    for i in range(t):
        if ret[i] == -1:
            outfile.write("Case #%d: IMPOSSIBLE\n" %(i+1))
        else:
            outfile.write("Case #%d: %s\n" %(i+1, ret[i]))