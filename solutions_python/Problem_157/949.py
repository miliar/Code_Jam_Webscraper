#!/usr/bin/python
#!/usr/bin/python
# -*-coding:Latin-1 -*
import sys
def Mat(a, sign, b):
	if a == '1':
		return (b, sign)
	if b == '1':
		return (a, sign)
	if a == 'i' and b == 'j':
		return ('k', sign)
	if a == 'j' and b == 'i':
		return ('k', -1 * sign)
	if a == 'k' and b == 'i':
		return ('j', sign)
	if a == 'i' and b == 'k':
		return ('j', -1 * sign)
	if a == 'j' and b =='k':
		return ('i', sign)
	if a == 'k' and b =='j':
		return ('i', -1 * sign)
	if a == 'i' and b == 'i':
		return ('1', -1 * sign)
	if a =='j' and b =='j':
		return ('1', -1 * sign)
	if a == 'k' and b =='k':
		return ('1', -1 * sign)

Test = input()
for c in range(0, Test):
    x, y = map(int, raw_input().split())
    z = map(str, raw_input())

    res = '1'
    sign = 1

    w = y

    aa = False
    bb = False
    cc = False

    for i in xrange(y):
        for j in z:
            res, sign = Mat(res, sign, j)

        if res == '1' and sign == 1:
            w = i + 1
            break;

    l = y % w

    first = '1'
    second = 1
    for i in xrange(2 * w):
        for j in z:
            first, second = Mat(first, second, j)
            if first == 'i' and second == 1:
                aa = True
            if (aa == True and first == 'k' and second == 1):
                bb = True


    if (l > 0):
        res = '1'
        sign = 1
        for i in xrange(l):
            for j in z:
                res, sign = Mat(res, sign,  j)

    if aa == True and bb== True and res == '1' and sign == -1:
        print "Case #%d: YES" % (c+1)
    else:
        print "Case #%d: NO" % (c+1)
