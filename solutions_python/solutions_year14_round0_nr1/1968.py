n = int(input())

for i in range(n):
    
    grid = []
    row = int(input()) - 1
    
    for x in range(4):
        grid.append(int(a) for a in input().split())
        
    first = set(grid[row])
    
    
    grid = []
    row = int(input()) - 1
    for x in range(4):
        grid.append(int(a) for a in input().split())
        
    second = set(grid[row])
    
    length = len(first.intersection(second))
    
    print("Case #" + str(i + 1) + ": ", end="")
    if length == 0:
        print("Volunteer cheated!")
    elif length == 1:
        print(first.intersection(second).pop())
    else:
        print("Bad magician!")