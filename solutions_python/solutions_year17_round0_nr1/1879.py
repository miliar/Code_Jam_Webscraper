fp = open('/Users/hareesh/Desktop/out.txt',"w")
for i in range(input()):
    s, n = raw_input().split()
    s = s.replace('-','0')
    s = s.replace('+','1')
    res = int('1'+s, base=2)
    n = int(n)
    mask = int('1'*n, base=2)
    flag = 1
    k = int('1'*(len(s)+1), base=2)
    count = 0
    for j in range(len(s)-n+2):
        bres = bin(res)
        bk = bin(k)
        bflag = bin(flag)
        if not (flag & res):
            res = res^mask
            count += 1
        flag <<= 1
        mask <<= 1
    # print 'Case #{}:'.format(i + 1),
    # print count if k == res else 'IMPOSSIBLE'
    fp.write(('Case #{}: ' + (str(count) if k == res else 'IMPOSSIBLE') + '\n').format(i + 1))
fp.close()