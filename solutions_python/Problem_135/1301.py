from copy import deepcopy
t = int(input())

def prov():
    cnt = 0
    k = 0
    for i in range(4):
        for j in range(4):
            if a[i] == b[j]:
                k = a[i]
                cnt += 1
    if cnt >= 2:
        return 'Bad magician!'
    elif cnt == 0:
        return 'Volunteer cheated!'
    else:
        return k
    


for i in range(t):
    a = []
    b = []
    for j in range(2):
        a1 = int(input())
        a1 -= 1
        for k in range(4):
            f = list(map(int, input().split()))
            if k == a1 and j == 0:
                a = deepcopy(f)
            if k == a1 and j == 1:
                b = deepcopy(f)
    print('Case #',i + 1,':',' ',prov(), sep = '')
                
                
    