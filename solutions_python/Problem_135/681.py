l = open('in')

n = int(l.readline())
for i in range(n):
    row1 = int(l.readline())
    l1 = [l.readline().split(),l.readline().split(),l.readline().split(),l.readline().split()]
    row2 = int(l.readline())
    l2 = [l.readline().split(),l.readline().split(),l.readline().split(),l.readline().split()]
    l3 = [i for i in l1[row1-1] if i in l2[row2-1]]
    result = ''
    if len(l3) == 1:
        result = l3[0]
    elif len(l3) > 1:
        result = 'Bad magician!'
    else:
        result = 'Volunteer cheated!'
    print("Case #"+str(i+1)+": "+result)
