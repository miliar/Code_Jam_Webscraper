def readInts():
    r = raw_input()
    s = r.split()
    return [int(ss) for ss in s]

def readString():
    r = raw_input()
    return r

dic = {}

def count(needle, haystack):
    if dic.has_key((needle, haystack)):
        return dic[(needle, haystack)]

    if not needle or not haystack:
        return 0

    n = needle[0]
    if len(needle) == 1:
        return haystack.count(n)

    h = haystack[0]
    
    if n == h:
        ans = count(needle[1:], haystack[1:]) + count(needle, haystack[1:])
    else:
        ans = count(needle, haystack[1:])
        
    dic[(needle, haystack)] = ans
    return ans
    
def main():
    n = readInts()[0]
    short = 'welcome to code jam'
    
    case = 1
    for i in range(n):
        global dic
        dic = {}
        s = readString()
        print 'Case #%d: %04d' % (case, count(short, s))
        case += 1

if __name__ == '__main__':
    main()