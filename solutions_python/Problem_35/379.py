def find_min (array, cood):
    i = cood[0]
    j = cood[1]
    minalt = 10000
    if i > 0 and minalt > array[i - 1][j]:
        cood[0] = i - 1
        cood[1] = j
        minalt = array[i - 1][j]
    if j > 0 and minalt > array[i][j - 1]:
        cood[0] = i
        cood[1] = j - 1
        minalt = array[i][j - 1]
    if j < w - 1 and minalt > array[i][j + 1]:
        cood[0] = i
        cood[1] = j + 1
        minalt = array[i][j + 1]
    if i < h - 1 and minalt > array[i + 1][j]:
        cood[0] = i + 1
        cood[1] = j
        minalt = array[i + 1][j]
    return minalt

n = int(raw_input())
for idx in range(n):
    h, w = raw_input().split(' ')
    # print h, w
    h = int(h)
    w = int(w)
    # print h+w
    array = []
    result = []
    for i in range(h):
        array.append(raw_input().split(' '))
        result.append([0] * w) 
    for i in range(h):
        for j in range(w):
            array[i][j] = int(array[i][j])

    label = 'a'
    for i in range(h):
        for j in range(w):
            lst = []
            cood = [i, j]
            while True:
                if result[i][j] != 0:
                    break
                lst.append(cood+[])
                std = array[cood[0]][cood[1]]
                minalt = find_min(array, cood)
                #print minalt
                #print lst
                if minalt >= std:
                    for cood0 in lst:
                        result[cood0[0]][cood0[1]] = label
                    label = chr(ord(label) + 1)
                    break
                elif result[cood[0]][cood[1]] != 0:
                    lbl = result[cood[0]][cood[1]]
                    for cood0 in lst:
                        result[cood0[0]][cood0[1]] = lbl
                    break
    print 'Case #%d:' % (int(idx) + 1)
    for row in result:
        print row[0],
        for i in row[1:]:
            print ' ' + str(i),
        print
        
            
