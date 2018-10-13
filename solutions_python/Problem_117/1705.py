def large(lawn):
    big = 0
    for i in lawn:
        for j in i:
            k = int(j)
            if k > big:
                big = k
    return big

def rallsame(li,k):
    global m
    if len(li) == 1:
        return [True, li[k]]
    for m in range(k):
        if li[m] != li[m+1]:
            return [False, 0]
    return [True, li[m]]

def check(lawn, size):
    big = str(large(lawn))
    lawn2 = [[big]*size[1]]*size[0]
    for i in range(size[0]):
        tmp = rallsame(lawn[i], size[1]-1)
        if not tmp[0]:
            continue
        else:
            lawn2[i] = [tmp[1]]*size[1]
    if lawn2 == lawn:
        return 'YES'
    for i in range(size[1]):
        li = ''
        for j in range(size[0]):
            li += lawn[j][i]
        tmp = rallsame(li, size[0]-1)
        if not tmp[0]:
            continue
        for k in range(size[0]):
            lawn2[k][i] = tmp[1]
    if lawn2 == lawn:
        return 'YES'
    else:
        return 'NO'

inf = open('B-small-attempt0.in', 'r')
outf = open('ans.in', 'w')

no = int(inf.readline())

for i in range(no):
    size = inf.readline().split()
    size[0] = int(size[0])
    size[1] = int(size[1])
    lawn = []
    for j in range(size[0]):
        lawn.append(inf.readline().split())
    ans = check(lawn, size)
    outf.write(('Case #{0}: '+ans+'\n').format(i+1))

outf.close()
inf.close()
