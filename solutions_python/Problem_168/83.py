directions = dict()
directions['.'] = 0
directions['^'] = 1
directions['>'] = 2
directions['v'] = 3
directions['<'] = 4

n = int(input())

def arrowCardinal(field,arrow,r,c):
    directions = []
    for row in range(arrow[0]+1,r):
        if field[row][arrow[1]]:
            directions.append(3)
            break
    for row in range(0,arrow[0]):
        if field[row][arrow[1]]:
            directions.append(1)
            break
    for col in range(arrow[1]+1,c):
        if field[arrow[0]][col]:
            directions.append(2)
            break
    for col in range(0,arrow[1]):
        #print((arrow[0],col))
        if field[arrow[0]][col]:
            directions.append(4)
            break    
    return directions
    
def f(field,r,c):
    arrows = []
    for row in range(r):
        for col in range(c):
            if field[row][col] != 0:
                arrows.append((row,col))
    ans = 0
    for arrow in arrows:
        x = arrowCardinal(field,arrow,r,c)
        if len(x) == 0:
            return "IMPOSSIBLE"
        if field[arrow[0]][arrow[1]] not in x:
            ans += 1
    return ans
            

for case in range(n):
    r,c = list(map(int,input().split()))
    field = []
    for i in range(r):
        field.append(list(map(lambda x: directions[x],input().rstrip('\n'))))
    print("Case #{0}: {1}".format(case+1,f(field,r,c)))
    

    
    

        