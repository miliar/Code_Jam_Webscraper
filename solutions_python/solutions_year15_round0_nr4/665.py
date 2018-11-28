inp = input("Enter the file name: ")
op = open(inp,'r')
file = op.read().split("\n")
T = eval(file[0])

for i in range(T):
    lst = file[i+1].split()
    X = eval(lst[0])
    R = eval(lst[1])
    C = eval(lst[2])
    if X == 1:
        print("Case #" + str(i+1) + ": " + "GABRIEL")
    else:
        if (R * C) % X != 0:
            print("Case #" + str(i+1) + ": " + "RICHARD")
        else:
            if (R * C) < (X * (X-1)):
                print("Case #" + str(i+1) + ": " + "RICHARD")
            else:
                print("Case #" + str(i+1) + ": " + "GABRIEL")
        
