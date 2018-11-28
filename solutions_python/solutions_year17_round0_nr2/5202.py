def processsmall(n):
    big = 0
    for i in range(1, (n+1)):
        if 0 in list(str(i)):
            continue
        else:
            if i == int(''.join(sorted(str(i)))):
                if i > big or big == 0:
                    big = i
    return big
#def processbig(n):
#    s = list(str(n))
#    p = s.index('0')
#    big = (n/10**(len(s)-p))*9
#    return big
    
t = int(raw_input())
for i in range(1, t+1):
    n = int(raw_input())
    if n < 1000000:
        bigtidy = processsmall(n)
    else:
        bigtidy = processbig(n)
    print 'Case #{}:'.format(i), bigtidy