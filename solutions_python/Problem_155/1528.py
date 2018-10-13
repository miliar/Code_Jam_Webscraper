import sys 
lines = sys.stdin.readlines()
for i in range((int(lines[0]))):
    s, p = lines[i+1].split()
    z = 0
    n = 0
    for j in range(len(p)):
        if p[j] == '0' and j >= n : 
            z += 1
            n += 1
        else: n += int(p[j])
        if n >= int(s): break
    print 'Case #'+str(i+1)+': '+str(z)
