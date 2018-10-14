from operator import xor

__author__ = 'sonych'

f = open("file.in")
lines = f.readlines()
f.close()

t = int(lines[0])
del lines[0]

q = 0
while q < t:
    n = int(lines[0])
    cb = lines[1]
    cb = cb.split()
    cv = []
    for i in range(n):
        cv.append(int(cb[i]))
    cv.sort()

    sum = 0
    sum_r = 0
    for i in range(n):
        sum = xor(cv[i],sum)
        sum_r += cv[i]

    if sum != 0:
        print "Case #" + str(q+1) + ': ' + 'NO'
    else:
        res = sum_r - cv[0]
        print "Case #" + str(q+1) + ': ' + str(res)

    del lines[0]
    del lines[0]
    q += 1
