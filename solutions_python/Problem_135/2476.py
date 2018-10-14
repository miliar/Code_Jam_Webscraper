data = []
with open("A-small.txt", "r") as f:
    for line in f:
        data.append(line.strip())

index = 0
T = int(data[index])
index += 1

for case in range(1, T+1):
    ans1 = int(data[index])
    index += 1
    
    for i in range(4):
        row = data[index]
        index += 1
        if i == ans1 - 1:
            row1 = [int(num) for num in row.split()]
            
    ans2 = int(data[index])
    index += 1
    
    for i in range(4):
        row = data[index]
        index += 1
        
        if i == ans2 - 1:
            row2 = [int(num) for num in row.split()]

    candidates = [num for num in row1 if num in row2]
    
    output = "Case #" + str(case) + ": "
    if len(candidates) == 1:
        output += str(candidates[0])
    elif len(candidates) > 1:
        output += "Bad magician!"
    else:
        output += "Volunteer cheated!"
    print(output)
