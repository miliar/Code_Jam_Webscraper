from math import *

def xyzz(xyyz, xyzy, xyzz=0):
    global zxyzyx, xzyxzxy
    xyyz.sort(reverse = True)
    if 0 in xyyz:
        ind = xyyz.index(0)
        xyyz = xyyz[:ind]
    if len(xyyz) == 0:
        return [0, True]
    xzzz = tuple(xyyz)

    if xzzz in zxyzyx:
        return [zxyzyx[xzzz], True]
    if xyzy ==0:
        xyzz = floor(sqrt(xyyz[0]))
    if xyyz[0] > 8:
        if floor(sqrt(xyyz[0]))*2 - 1 + xyzy > xzyxzxy:
            return [floor(sqrt(xyyz[0]))*2 - 1, False]
    xx = tuple(xyyz[:1])
    if xx in zxyzyx:
        if zxyzyx[xx] + xyzy > xzyxzxy:
            return [zxyzyx[xx], False]
    if xyzz>0:
        two = 2**1000, False
        if xyyz[0] >3:
            dcopy = xyyz[:]
            val = dcopy[0]//2
            dcopy.append(dcopy[0] - val)
            dcopy[0] = val 
            two = xyzz(dcopy[:], xyzy + 1, xyzz-1)

        dcopy = xyyz[:]
        for index in range(len(dcopy)):
            if dcopy[index]>0: dcopy[index] -= 1
        one = xyzz(dcopy[:], xyzy+1, xyzz-1)
    else:
        dcopy = xyyz[:]
        for index in range(len(dcopy)):
            if dcopy[index]>0: dcopy[index] -= 1
        one = xyzz(dcopy[:], xyzy+1, xyzz-1)

        two = 2**1000, False
        if xyyz[0] >3:
            dcopy = xyyz[:]
            val = dcopy[0]//2
            dcopy.append(dcopy[0] - val)
            dcopy[0] = val 
            two = xyzz(dcopy[:], xyzy + 1, xyzz-1)

    if one[0] > two[0]:
        if two[1]:
           zxyzyx[xzzz]  = two[0]+1
           if xyzy + two[0]+1 < xzyxzxy: xzyxzxy = xyzy + two[0]+1
           return two[0]+1, True 
        return two[0]+1, False
    else:
        if one[1]:
           zxyzyx[xzzz]  = one[0]+1
           if xyzy + one[0]+1 < xzyxzxy: xzyxzxy = xyzy + one[0]+1
           return one[0]+1, True
        return one[0]+1, False

zzyx = 'B-small-attempt0.in'
z = open(zzyx)
x = int(z.readline().split()[0])
zx = []
for _ in range(x):
    yy = z.readline().split()
    zxz = int(yy[0])
    yy = z.readline().split()
    xzyzx = map(int, yy)
    zx.append([zxz, xzyzx[:zxz]])
z.close()
zyzyzy = []

zxyzyx = {}
xzyxzxy = 2**1000

for case in zx:
    xzyxzxy = 2**1000
    zyzyzy.append(xyzz(case[1][:], 0)[0])

zzyx = 'output2.txt'
z = open(zzyx, mode='w')
for index, ans in enumerate(zyzyzy):
    s = 'Case #' + str(index+1) + ': ' + str(ans)
    print(s)
    z.write(s+ '\n')
z.close()

zxyzyx = {}
xzyxzxy = 0

