def readInts():
    s = raw_input()
    return [int(ss) for ss in s.split()]

def dec(n, b):
    result = []
    while n != 0:
        r = n % b
        n /= b
        result.append(r)
    return result

def ssquare(a):
    return sum([i * i for i in a])

def isHappy(n, b):
    used = {}

    ss = n
    while True:
        d = dec(ss, b)
        ss = ssquare(d)
        if ss == 1:
            return True
        
        if ss in used.keys():
            return False
        
        used[ss] = True

def commonHappy(bases):
    i = 2
    while True:
        happy = True
        for b in bases:
            if not isHappy(i, b):
                happy = False
                break
        
        if happy:
            return i
        
        i += 1

def test():
    print commonHappy([10, 7, 8])
    # print isHappy(12, 10)
    
def main():
    n = readInts()[0]
    case = 1
    for i in range(n):
        bases = readInts()
        ans = commonHappy(bases)
        print 'Case %s: %s' % (case, ans)
        case += 1
        
if __name__ == '__main__':
    main()
    # test()
