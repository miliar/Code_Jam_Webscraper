def digit(s):
    s=list(s)
    num=[]
    while s:
        if 'Z' in s:
            temp=s.count('Z')
            for i in xrange(temp):
                s.pop(s.index('Z'))
                s.pop(s.index('E'))
                s.pop(s.index('R'))
                s.pop(s.index('O'))
                num.append(0)
        if 'W' in s:
            temp=s.count('W')
            for i in xrange(temp):
                s.pop(s.index('T'))
                s.pop(s.index('W'))
                s.pop(s.index('O'))
                num.append(2)
        if 'G' in s:
            temp=s.count('G')
            for i in xrange(temp):
                s.pop(s.index('T'))
                s.pop(s.index('H'))
                s.pop(s.index('E'))
                s.pop(s.index('I'))
                s.pop(s.index('G'))
                num.append(8)
        if 'X' in s:
            temp=s.count('X')
            for i in xrange(temp):
                s.pop(s.index('S'))
                s.pop(s.index('I'))
                s.pop(s.index('X'))
                num.append(6)
        if 'U' in s:
            temp=s.count('U')
            for i in xrange(temp):
                s.pop(s.index('F'))
                s.pop(s.index('O'))
                s.pop(s.index('U'))
                s.pop(s.index('R'))
                num.append(4)
        if 'S' in s:
            temp=s.count('S')
            for i in xrange(temp):
                s.pop(s.index('S'))
                s.pop(s.index('E'))
                s.pop(s.index('V'))
                s.pop(s.index('E'))
                s.pop(s.index('N'))
                num.append(7)
        if 'V' in s:
            temp=s.count('V')
            for i in xrange(temp):
                s.pop(s.index('F'))
                s.pop(s.index('I'))
                s.pop(s.index('V'))
                s.pop(s.index('E'))
                num.append(5)

        if 'I' in s:
            temp=s.count('I')
            for i in xrange(temp):
                s.pop(s.index('N'))
                s.pop(s.index('I'))
                s.pop(s.index('N'))
                s.pop(s.index('E'))
                num.append(9)
        if 'N' in s:
            temp = s.count('N')
            for i in xrange(temp):
                s.pop(s.index('O'))
                s.pop(s.index('N'))
                s.pop(s.index('E'))
                num.append(1)
        if 'R' in s:
            temp = s.count('R')
            for i in xrange(temp):
                s.pop(s.index('T'))
                s.pop(s.index('H'))
                s.pop(s.index('R'))
                s.pop(s.index('E'))
                s.pop(s.index('E'))
                num.append(3)
    num.sort()
    num=map(str,num)
    return ''.join(num)
for i in xrange(int(raw_input().strip())):
    print "Case #%d: %s" %(i+1,digit(raw_input().strip()))