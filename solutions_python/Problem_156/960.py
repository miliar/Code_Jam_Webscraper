import sys
from math import *
sys.setrecursionlimit(2000)
def time(diners, passedtime, max=0):
    global di, min
    diners.sort(reverse = True)
    if 0 in diners:
        ind = diners.index(0)
        diners = diners[:ind]
    if len(diners) == 0:
        return [0, True]
    dinerkey = tuple(diners)

    if dinerkey in di:
        return [di[dinerkey], True]
    if passedtime ==0:
        max = floor(sqrt(diners[0]))
    xx = tuple(diners[:1])
    if xx in di:
        if di[xx] + passedtime > min:
            return [di[xx], False]
    if max>0:
        two = 2**1000, False
        if diners[0] >3:
            dcopy = diners[:]
            val = dcopy[0]//2
            dcopy.append(dcopy[0] - val)
            dcopy[0] = val 
            two = time(dcopy[:], passedtime + 1, max-1)
        three = 2**1000, False
        if diners[0] >3:
            dcopy = diners[:]
            val = dcopy[0]//2 -1
            dcopy.append(dcopy[0] - val)
            dcopy[0] = val 
            three = time(dcopy[:], passedtime + 1, max-1)
        dcopy = diners[:]
        for index in range(len(dcopy)):
            if dcopy[index]>0: dcopy[index] -= 1
        one = time(dcopy[:], passedtime+1, max-1)
    else:
        dcopy = diners[:]
        for index in range(len(dcopy)):
            if dcopy[index]>0: dcopy[index] -= 1
        one = time(dcopy[:], passedtime+1, max-1)

        two = 2**1000, False
        if diners[0] >3:
            dcopy = diners[:]
            val = dcopy[0]//2
            dcopy.append(dcopy[0] - val)
            dcopy[0] = val 
            two = time(dcopy[:], passedtime + 1, max-1)
        three = 2**1000, False
        if diners[0] >3:
            dcopy = diners[:]
            val = dcopy[0]//2 -1
            dcopy.append(dcopy[0] - val)
            dcopy[0] = val
            three = time(dcopy[:], passedtime + 1, max-1)
    minnn = three
    if one[0]<minnn[0]:
        minnn = one
    if two[0]<minnn[0]:
        minnn = two
    if minnn[1]:
        di[dinerkey] = minnn[0]+1
        if passedtime + minnn[0]+1 < min: min = passedtime + minnn[0]+1
        return minnn[0]+1, True
    return minnn[0]+1, False
    

di = {
        ( 2 ,) : 2,
        ( 3 ,) : 3,
        ( 4 ,) : 3,
        ( 5 ,) : 4,
        ( 6 ,) : 4,
        ( 7 ,) : 5,
        ( 8 ,) : 5,
        ( 9 ,) : 5,
        ( 10 ,) : 6,
        ( 11 ,) : 6,
        ( 12 ,) : 6,
        ( 13 ,) : 7,
        ( 14 ,) : 7,
        ( 15 ,) : 7,
        ( 16 ,) : 7,
        ( 17 ,) : 8,
        ( 18 ,) : 8,
        ( 19 ,) : 8,
        ( 20 ,) : 8,
        ( 21 ,) : 9,
        ( 22 ,) : 9,
        ( 23 ,) : 9,
        ( 24 ,) : 9,
        ( 25 ,) : 10,
        ( 26 ,) : 10,
        ( 27 ,) : 10,
        ( 28 ,) : 10,
        ( 29 ,) : 10,
        ( 30 ,) : 10,
        ( 31 ,) : 10,
        ( 32 ,) : 10,
        ( 33 ,) : 10,
        ( 34 ,) : 10,
        ( 35 ,) : 10,
        ( 36 ,) : 10,
        ( 37 ,) : 10,
        ( 38 ,) : 10,
        ( 39 ,) : 10,
        ( 40 ,) : 10,
        ( 41 ,) : 10,
        ( 42 ,) : 10,
        ( 43 ,) : 10,
        ( 44 ,) : 10,
        ( 45 ,) : 10,
        ( 46 ,) : 10,
        ( 47 ,) : 10,
        ( 48 ,) : 10,
        ( 49 ,) : 11,
        ( 50 ,) : 10,
        ( 51 ,) : 10,
        ( 52 ,) : 10,
        ( 53 ,) : 10,
        ( 54 ,) : 10,
        ( 55 ,) : 10,
        ( 56 ,) : 10,
        ( 57 ,) : 10,
        ( 58 ,) : 10,
        ( 59 ,) : 10,
        ( 60 ,) : 10,
        ( 61 ,) : 10,
        ( 62 ,) : 10,
        ( 63 ,) : 10,
        ( 64 ,) : 10,
        ( 65 ,) : 11,
        ( 66 ,) : 11,
        ( 67 ,) : 11,
        ( 68 ,) : 11,
        ( 69 ,) : 11,
        ( 70 ,) : 11,
        ( 71 ,) : 11,
        ( 72 ,) : 11,
        ( 73 ,) : 11,
        ( 74 ,) : 11,
        ( 75 ,) : 11,
        ( 76 ,) : 11,
        ( 77 ,) : 11,
        ( 78 ,) : 11,
        ( 79 ,) : 11,
        ( 80 ,) : 11,
        ( 81 ,) : 12,
        ( 82 ,) : 12,
        ( 83 ,) : 12,
        ( 84 ,) : 12,
        ( 85 ,) : 12,
        ( 86 ,) : 12,
        ( 87 ,) : 12,
        ( 88 ,) : 12
    }
min = 2**1000

#for i in range(24,128):
#    print('(', i, ',) :', time([i], 0)[0], ',')

filename = 'B-small-attempt0.in'
f = open(filename)
T = int(f.readline().split()[0])
cases = []
for _ in range(T):
    line = f.readline().split()
    D = int(line[0])
    line = f.readline().split()
    diners = list(map(int, line))
    cases.append([D, diners[:D]])
f.close()
answers = []

for index, case in enumerate(cases):
    if index == 43:
        pass
    min = 2**1000
    answers.append(time(case[1][:], 0)[0])

filename = 'output2.txt'
f = open(filename, mode='w')
for index, ans in enumerate(answers):
    s = 'Case #' + str(index+1) + ': ' + str(ans)
    print(s)
    f.write(s+ '\n')
f.close()

di = {}
min = 0

