T = input()
ansstr = 'Case #{0}: {1}'
ansbad = 'Bad magician!'
anscht = 'Volunteer cheated!'
ans = 0

for i in range(T):
    ans = 0
    a1 = input() - 1
    c = list()
    for j in range(4):
        for k in map(int, raw_input().split()):
            if j == a1:
                c.append(k)
    a2 = input() - 1
    for j in range(4):
        for k in map(int, raw_input().split()):
            if j == a2:
                if c.count(k) == 1 and ans == 0:
                    ans = k
                elif c.count(k) == 1 and ans != 0: 
                    ans = -1
                    break
    if ans == -1:
        print(ansstr.format(i+1, ansbad))
    elif ans == 0:
        print(ansstr.format(i+1, anscht))
    else:
        print(ansstr.format(i+1, ans))



