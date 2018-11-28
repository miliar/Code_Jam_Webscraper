


res = []

def intersection(lst1, lst2):
    res = []
    for i in lst2:
        if i in lst1:
            res.append(i)
    return res

testcases = int(raw_input())
for i in range(testcases):
    rowNo1 = int(raw_input())
    row11 = map(int, raw_input().split(' '))
    row12 = map(int, raw_input().split(' '))
    row13 = map(int, raw_input().split(' '))
    row14 = map(int, raw_input().split(' '))
    row1 = {1: row11, 2:row12, 3:row13, 4:row14}

    rowNo2 = int(raw_input())
    row21 = map(int, raw_input().split(' '))
    row22 = map(int, raw_input().split(' '))
    row23 = map(int, raw_input().split(' '))
    row24 = map(int, raw_input().split(' '))
    row2 = {1:row21, 2:row22, 3:row23, 4:row24}

    intersect = intersection(row1[rowNo1], row2[rowNo2])
    if len(intersect) == 1:
        res.append(intersect[0])
    elif len(intersect) > 1:
        res.append('b')
    else:
        res.append('c')

for i in range(len(res)):
    if type(res[i]) == int:
        print 'Case #' + str(i+1) + ': ' + str(res[i])
    elif res[i] == 'b':
        print 'Case #' + str(i+1) + ': ' + 'Bad magician!'
    else:
        print 'Case #' + str(i+1) + ': ' + 'Volunteer cheated!'
        
        
    
