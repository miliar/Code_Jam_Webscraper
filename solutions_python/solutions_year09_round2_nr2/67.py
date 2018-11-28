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

def work(num):
    for i in range(1, len(num)):
        if num[i] < num[i - 1]:
            break
    
    for j in range(i):
        if num[j] > num[i]:
            break
    
    tmp = num[i]
    num[i] = num[j]
    num[j] = tmp
    
    tmp = num[:i]
    tmp.sort(reverse=True)
    
    for k in range(i):
        num[k] = tmp[k]

def present(num):
    result = 0
    for i in range(len(num) - 1, -1, -1):
        result *= 10
        result += num[i]
        
    return result

def main():
    t = readInts()[0]
    case = 1
    for i in range(t):
        n = readInts()[0]
        num = dec(n, 10)
        num.append(0)
        
        work(num)
        print 'Case #%s: %s' % (case, present(num))
        case += 1
        
def test():
    a = [0, 0, 1, 0]
    work(a)
    print a
    print present(a)
    pass

if __name__ == '__main__':
    main()
    # test()
