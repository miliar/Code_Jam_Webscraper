import sys

def b(N):
    length = len(N)

    increasing = True
    point = 0
    for i in range(1,length):
        if int(N[i]) < int(N[i-1]):
            increasing = False
            break
        elif int(N[i]) > int(N[i-1]):
            point = i

    if increasing:
        return N

    if point == 0 and N[0] == '1':
        return '9' * (length - 1)

    return N[:point] + str(int(N[point])-1) + '9' * (length - point - 1)

n = int(input())
for i in range(n):
    N = input()
    print('Case #' + str(i + 1) + ': ', end='')
    print(b(N))


    
            
    
    
    
