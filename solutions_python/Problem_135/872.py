T = int(input())
for t in range(T):
    r1 = int(input())
    mat1 = [[int(elt) for elt in input().split()]for i in range(4)]
    s1 = set(mat1[r1-1])
    
    r2 = int(input())
    mat2 = [[int(elt) for elt in input().split()]for i in range(4)]
    s2 = set(mat2[r2-1])
    
    s = s1.intersection(s2)
    
    print('Case #',t+1,': ',sep='',end='')
    if len(s) == 0:
        print('Volunteer cheated!')
    elif len(s) == 1:
        print(s.pop())
    else:
        print('Bad magician!')        
