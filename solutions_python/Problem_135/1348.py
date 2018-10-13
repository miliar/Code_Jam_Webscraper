def getint():
    return int(raw_input())
    
def getints():
    return [int(x) for x in raw_input().split()]
    
def answer():
    rc = None
    ans = getint()
    for i in range(4):
        y = getints()
        if i+1 == ans:
            rc = y
    return rc
    
def test(n):
    x = set(answer())
    y = set(answer())
    z = x.intersection(y)
    if len(z) == 1:
        ans = z.pop()
    elif len(z) > 1:
        ans = 'Bad magician!'
    else:
        ans = 'Volunteer cheated!'
    print 'Case #%d: %s'%(n, ans)

def main():
    T = getint()
    for i in range(T):
        test(i+1)

if __name__ == '__main__':
    main()