inp = input("Enter the file name: ")
op = open(inp,'r')
file = op.read().split("\n")
T = eval(file[0])
temp = 1
for i in range(T):
    lst = file[temp].split()
    maximum = eval(lst[0])
    audience = list(lst[1])
    minAdded = audCount = total = 0
    for j in range (maximum):
        if eval(audience[j]) > 0:
            audCount += eval(audience[j])
        total = audCount + minAdded
        if total < (j+1) and eval(audience[j+1]) != 0:
            minAdded += (j+1) - total
    print("Case #" + str(i + 1) + ": " + str(minAdded))
    temp += 1
