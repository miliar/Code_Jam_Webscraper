f=open('A-small-attempt0.in')
o=open('result.txt','w')

T=int(f.readline())
case=1
while case<=T:
    row1 = int(f.readline())
    r = 1
    while r<row1:
        f.readline()
        r += 1
    answers1 = f.readline().strip().split(' ')
    while r<4:
        f.readline()
        r += 1

    row2 = int(f.readline())
    r = 1
    while r<row2:
        f.readline()
        r += 1
    answers2 = f.readline().strip().split(' ')
    while r<4:
        f.readline()
        r += 1

    num=0
    for a in answers1:
        if a in answers2:
            ans = a
            num += 1
    if num == 0:
        ans = 'Volunteer cheated!'
    if num > 1:
        ans = 'Bad magician!'
    o.write('Case #{0}: {1}\n'.format(str(case),ans))
    
    case += 1

f.close()
o.close()
