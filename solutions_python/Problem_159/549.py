__author__ = 'Victor'

fi = open('A-large (1).in', 'r')
fo = open('MushroomMaster.out', 'w')

t = int(next(fi))

for i in range(t):
    n = int(next(fi))
    case = [int(x) for x in next(fi).strip().split(' ')]
    way1=0
    way2=0
    ratio = 0
    for j in range(n):
        if j == n-1:
            continue
        if case[j] > case[j+1]:
            way1 += case[j]-case[j+1]
            if case[j]-case[j+1] > ratio:
                ratio = case[j]-case[j+1]

    for k in range(n):
        if k == n-1:
            continue
        if case[k] <= ratio:
            way2+= case[k]
        else:
            way2+=ratio



    fo.write('Case #%d: ' %(i+1))
    fo.write('%d ' % way1)
    fo.write('%d\n' % way2)





fi.close()
fo.close()