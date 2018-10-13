def size(a):
    cur = 0
    sizeA = 0
    while a / (10 ** cur) > 0:
        sizeA = sizeA + 1
        cur = cur + 1
    return sizeA

def isRecycled(a, b):
    sz = size(a)
    left = 1
    while left < sz:
        oleft = 10 ** left
        right = sz - left
        oright = 10 ** right
        tmp = (a % oright) * (10 ** left)
        tmp = tmp + a / (10 ** right)
        if tmp == b:
            return 1
        left = left + 1
    return 0

def result(a, b):
    res = 0
    while a < b:
        cur = a + 1
        while cur <= b:
            res = res + isRecycled(a, cur)
            cur = cur + 1
        a = a + 1
    return res

fi = open('./B.in', 'r')
fo = open('./B.out', 'w')

test = int(fi.readline())
for i in range(test):
    tmp = fi.readline().split(' ')
    fo.write('Case #%i: %i\n' % (i + 1, result(int(tmp[0]), int(tmp[1]))))

fo.close()
fi.close()
