file = open('./B-large.in')
new_file =  open('./B-large.out', 'w')

testcases = [x.rstrip() for x in file.readlines()]

def check_lawn(start, lawn, move):
    new_lawn = []
    num = len(lawn[0])
    check = [start for q in range(num)]
    for x in lawn:
        if check != x:
            new_lawn.append(x)
        if check == x:
            move = True
    return new_lawn, move
    
def rotate(lawn):
    num = len(lawn[0])
    new_lawn = []
    for i in range(num):
        arrg = [a[i] for a in lawn]
        new_lawn.append(arrg)
    return new_lawn

n = 1

for i in range(int(testcases[0])):
    size = testcases[n]
    size = [int(x) for x in size.split()]
    lawn = [testcases[n+j+1].split() for j in range(size[0])]
    for a in range(len(lawn)):
        for b in range(len(lawn[a])):
            lawn[a][b] = int(lawn[a][b])
    starts = []
    for x in lawn:
        for a in x:
            if a not in starts:
                starts.append(a)
    starts = sorted(starts)
    for start in starts:
        move = False
        lawn, move = check_lawn(start, lawn, move)
        if lawn:
            lawn = rotate(lawn)
            lawn, move = check_lawn(start, lawn, move)
        if lawn:
            lawn = rotate(lawn)
        if move == False:
            new_file.write('Case #%s: NO\n' % (i+1))
            break
        if lawn == []:
            new_file.write('Case #%s: YES\n' % (i+1))
            move = False
            break
        if move == True and start==starts[-1]:
            new_file.write('Case #%s: NO\n' % (i+1))
        
    n = size[0] + n + 1
file.close()
new_file.close()