import sys

f = open('A-large.in')

T = int(f.readline())
for i in range(T):
    line = f.readline().split()
    max_shy = int(line[0])
    shy = list()
    for c in line[1]:
        shy.append(int(c))
    ans = 0
    p = 1
    cur_total = shy[0]
    while p<=max_shy:
        if shy[p]>0 and cur_total<p:
            temp = p-cur_total
            ans += temp
            cur_total += temp
        cur_total += shy[p]
        p += 1
    print 'Case #{0}: {1}'.format(i+1, ans)

    
