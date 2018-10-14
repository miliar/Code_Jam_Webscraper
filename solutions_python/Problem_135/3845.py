def case(cisloc):
    r=int(input())-1
    st1=set()
    for i in range(4):
        if r == i:
            st1 = set([int(i) for i in input().split(' ')])
        else:
            input()
    r=int(input())-1
    st2=set()
    for i in range(4):
        if r == i:
            st2 = set([int(i) for i in (input().split(' '))])
        else:
            input()
    sz=len(st1.intersection(st2))
    if sz==0:
        print('Case #',cisloc, ': ', 'Volunteer cheated!' ,sep='', end='')
    if sz==1:
        print('Case #',cisloc, ': ', st1.intersection(st2).pop() ,sep='', end='')
    if sz>=2:
        print('Case #',cisloc, ': ', 'Bad magician!' ,sep='', end='')


n = int(input())
for i in range(n):
    case(i+1)
    if i!=n-1:
        print()
# print('Case #',cisloc, ': ', c[0]+1, ' ', c[1]+1 ,sep='', end='')
