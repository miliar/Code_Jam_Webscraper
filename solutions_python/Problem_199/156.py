def invert(ch):
    if ch=='+':
        return '-'
    elif ch=='-':
        return '+'
    else:
        return '?'
def f(line):
    row,n = line.split(' ')
    n = int(n)
    count = 0
    for i in xrange(len(row)-n+1):
        if row[i] == '-':
            row = row[:i] + ''.join(map(invert,row[i:i+n])) + row[i+n:]
            count += 1
            # print row,count
    if all(ch=='+' for ch in row):
        return count
    else:
        return 'IMPOSSIBLE'
        
T = int(raw_input())
for i in xrange(1,T+1):
    print "Case #%d: %s" % (i, f((raw_input())))
    
    # 5
    # 0
    # 1
    # 2
    # 11
    # 1692Square Brackets [ ] | English Club