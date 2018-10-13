def readInts():
    r = raw_input()
    s = r.split()
    return [int(ss) for ss in s]

def readString():
    r = raw_input()
    return r

def mysplit(s):
    result = []
    tmp = []

    state = 'outer'
    for i in range(len(s)):
        if s[i] == '(':
            state = 'inner'
        elif s[i] == ')':
            state = 'outer'
            result.append(tmp)
            tmp = []
        else:
            if state == 'inner':
                tmp.append(s[i])
            else:
                result.append([s[i]])
                

    return result

def match(word, rule):
    if len(word) != len(rule):
        return False

    for i in range(len(word)):
        w = word[i]
        if w not in rule[i]:
            return False
    return True

def main():
    l, d, n = readInts()

    dic = []
    for i in range(d):
        s = readString()
        dic.append(s)
    
    rules = []
    for i in range(n):
        s = readString()
        rules.append(mysplit(s))

    case = 1
    for r in rules:
    
        count = 0
        for d in dic:
            if match(d, r):
                count += 1

        print 'Case #%d: %d' % (case, count)
        case += 1

if __name__ == '__main__':
    main()
    # test2()
