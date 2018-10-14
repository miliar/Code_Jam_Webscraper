import bisect

T = int(raw_input())
case_number = 1
while case_number <= T:
    line = raw_input().split()
    n = int(line[0])
    k = int(line[1])
    spaces = {n: 1}
    if k == n:
        k = l = r = 0
    while k:
        k -= 1
        m = max(spaces.keys())
        spaces[m] -= 1
        if spaces[m] == 0:
            del spaces[m]
        l = m/2 + m%2 - 1
        r = m/2
        if l in spaces:
            spaces[l] += 1
        else:
            spaces[l] = 1
        if r in spaces:
            spaces[r] += 1
        else:
            spaces[r] = 1

        #print spaces
    print 'Case #{0}: {1} {2}'.format(case_number, max(l, r), max(min(l,r), 0))
    case_number += 1
exit()



# works only for small set
T = int(raw_input())
case_number = 1
while case_number <= T:
    line = raw_input().split()
    n = int(line[0])
    k = int(line[1])
    b = [1] + [0]*n + [1]
    ones = [0, len(b)-1]
    #print b
    while k:
        k -= 1
        m = ones[1] - ones[0] - 1
        for i in range(1, len(ones)):
            m = max(m, ones[i]-ones[i-1] - 1)
        for i in range(1, len(ones)):
            if ones[i] - ones[i-1] - 1 == m:
                a = ones[i-1]
                break

        l = m/2 + m%2 - 1
        r = m/2
        try:
            b[a+l+1] = 1
        except:
            l = r = 0
            break
        ones.append(a+l+1)
        ones.sort()
        #print b, ones, a, m, l, r
    print 'Case #{0}: {1} {2}'.format(case_number, max(l, r), min(l,r))
    case_number += 1

