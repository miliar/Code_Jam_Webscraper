def val(x):
    if x == '+':
        return 0
    return 1

n = int(raw_input(''));
for j in range(n):
    t = raw_input('')
    t = t.split(' ')
    k = int(t[1])
    s = t[0]
    flips = 0
    fl = []
    count = 0
    n1 = len(s)
    br = 0
    
    for i in range(k):
        if (count +val(s[i]))%2 != 0:
            if i >= n1 - k +1:
                br = 1
                break
            fl.append(1)
            flips += 1
            count += 1
        else:
            fl.append(0)

    if br == 1:
        print 'Case #' + str(j+1) + ': IMPOSSIBLE'
        continue

    for i in range(k,n1-k+ 1):
        count = count - fl[i - k]
        if (count +val(s[i]))%2 != 0:
            if i >= n1 - k +1:
                br = 1
                break
            fl.append(1)
            flips += 1
            count += 1
        else:
            fl.append(0)

    if br == 1:
        print 'Case #' + str(j+1) + ': IMPOSSIBLE'
        continue
        
        
    for i in range(n1-k+1,n1):
        count = count - fl[i-k]
        if (count +val(s[i]))%2 != 0:
            br = 1
            break
    if br == 1:
        print 'Case #' + str(j+1) + ': IMPOSSIBLE'
        continue
    else:
        print 'Case #' + str(j+1) + ': ' + str(flips)
            
            

            