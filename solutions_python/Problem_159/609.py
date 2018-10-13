f = open('A-large.in')
#f = open('test.in')
count = int(f.readline())
output = ''
for x in xrange(1, count + 1):
    platesCount = int(f.readline())
    arr = f.readline().split()
    case1 = 0
    case2 = 0
    case2MaxGap = 0
    for i in xrange(0, platesCount - 1):
        curPlate = int(arr[i])
        nextPlate = int(arr[i+1])
        gap = curPlate - nextPlate
        case2MaxGap = max(case2MaxGap, gap)
        if gap > 0:
            case1 += gap
    for j in xrange(0, platesCount - 1):
        curPlate = int(arr[j])
        if curPlate < case2MaxGap:
            case2 += curPlate
        else:
            case2 += case2MaxGap
    output += 'Case #' + str(x) + ': ' + str(case1) + ' ' + str(case2) + '\n'

print(output)
newf = open('output.txt','w')
newf.write(output)
