
def check(l):
    for i in range(len(l)-1):
        if int(l[i]) < int(l[i+1]):
            return False
    return True


def getnum(l):
    i=0
    while i < len(l)-1:
        if int(l[i]) > int(l[i+1]):
            break
        i += 1
    if i == len(l) - 1:
        return ''.join(l)
    
    while i > 0:
        if int(l[i]) > int(l[i-1]):
            break
        i -= 1
    
    if i == 0:
        if l[0] == '1':
            return '9'*(len(l)-1)
        else:
            return "%d%s" % (int(l[0])-1, '9'*(len(l)-1))
    
    return "%s%d%s" % (''.join(l[:i]), int(l[i])-1, '9'*(len(l)-i-1))


t = int(raw_input())
for i in xrange(1, t + 1):
    line = raw_input()
    print "Case #{}: {}".format(i, getnum(list(line)))
