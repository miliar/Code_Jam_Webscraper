
def main():
    fo = open('a.in')
    content = fo.read().strip()
    fo.close()

    contents = content.split('\n')
    
    #t = int(contents[0])

    fo = open('a.out', 'w')
    items = contents[1:]
    for i in range(len(items)):
        nvalue = calculateNvalue(items[i])
        print('Case #%s: %s' % (i+1, nvalue))
        fo.write('Case #%s: %s\n' % (i+1, nvalue))
    fo.close()

def calculateNvalue(item):
    nvalue = 0
    name = list(item.split(' ')[0])
    n = int(item.split(' ')[1])
    for i in range(n, len(name) + 1):
        for j in range(len(name) - i + 1):
            ss = name[j:j+i]
            if isNvalue(ss, n):
                nvalue += 1
    return nvalue

def isNvalue(ss, n):
    count = 0
    for i in range(len(ss)):
        if ss[i] in ['a', 'e', 'i', 'o', 'u']:
            count = 0
        else:
            count += 1
            if count >= n:
                return True
    return False

if __name__ == '__main__':
    main()

