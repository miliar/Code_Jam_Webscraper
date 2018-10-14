def solve(input):
    
    # Fill below
    for j in range(len(input[0])):
        for i in range(len(input)-1):
            if input[i+1][j] == "?" and input[i][j] != "?":
                input[i+1][j] = input[i][j]
                
    # Fill above
    for j in range(len(input[0])):
        for i in range(len(input)-1, 0, -1):
            if input[i-1][j] == "?" and input[i][j] != "?":
                input[i-1][j] = input[i][j]
    
    # Fill left
    for j in range(len(input[0])-1, 0, -1):
        for i in range(len(input)):
            if input[i][j-1] == "?" and input[i][j] != "?":
                input[i][j-1] = input[i][j]
    
    # Fill right
    for j in range(len(input[0])-1):
        for i in range(len(input)):
            if input[i][j+1] == "?" and input[i][j] != "?":
                input[i][j+1] = input[i][j]                
    
    
    for i in range(len(input)):
        input[i] = "".join(input[i])
    return "\n".join(input)


with open("A-large.in") as f:
    i = 1
    with open("A-large.out", "w") as w:
        f.readline()
        done = False
        while not done:
            case = [int(c) for c in f.readline().strip().split()]
            if len(case) != 2:
                break
            grid = []
            for j in range(case[0]):
                grid.append([c for c in f.readline().strip()])
            answer = solve(grid)
            print("Case #{0}:\n{1}".format(i, answer))
            w.write("Case #{0}:\n{1}\n".format(i, answer))
            i += 1