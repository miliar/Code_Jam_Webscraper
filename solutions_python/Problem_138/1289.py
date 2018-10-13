def getint():
    return int(raw_input())
    
def getlist():
    return [float(x) for x in raw_input().split()]
    
def test(n):
    N = getint()
    A = sorted(getlist())
    B = sorted(getlist())
    _B = list(B)
    x = y = 0
    for a in A:
        for b in _B:
            if b > a:
                _B.remove(b)
                break
        else:
            _B.pop(0)
            y += 1
    
    for i in A:
        if i < B[0]:
            B.pop(-1)
        else:
            B.pop(0)
            x += 1
        
    print 'Case #%d: %d %d'%(n, x, y)

def main():
    T = getint()
    for i in range(T):
        test(i+1)

if __name__ == '__main__':
    main()