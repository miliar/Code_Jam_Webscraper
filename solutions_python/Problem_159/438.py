def solve(s):
    result = [0,0]
    m1 = 0
    for i in range(len(s)-1):
        m1 += max(s[i]-s[i+1], 0)
    result[0] = m1
    m2 = 0
    minrate = 0
    for i in range(len(s)-1):
        minrate = max(minrate, s[i]-s[i+1])
    for i in range(len(s)-1):
        m2 += min(minrate, s[i])
    result[1] = m2
    return result 

with open('c:\\python27\\codejam\\outputs.out', 'w') as w, open('c:\\python27\\codejam\\A-large.in') as r:
    cases = int(r.readline())
    for case in range(1, cases+1):
        x = r.readline()
        shrooms = [int(x) for x in r.readline().split()]
        t = solve(shrooms)
        w.write('Case #{0}: {1} {2}\n'.format(str(case), str(t[0]), str(t[1])))

