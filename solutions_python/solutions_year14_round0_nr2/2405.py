data = []
with open("B-large-IN.in", "r") as f:
    for line in f:
        data.append(line.strip())

index = 0
T = int(data[index])
index += 1

output = ""
for case in range(1, T+1):
    nums = [float(num) for num in data[index].split()]
    index += 1

    C = nums[0]
    F = nums[1]
    X = nums[2]

    time = 0
    cookies = 0
    income = 2
    oldGoalTime = X
    while cookies < X:
##        print(time)
        farmTime = time + (C - cookies) / income
        goalTime = time + (X - cookies) / income
##        print("time:", time, "farmTime:", farmTime, "goalTime:", goalTime)
        if oldGoalTime < goalTime:
            time = oldGoalTime
            cookies = X
        else:
            time = farmTime
            cookies = 0
            income += F
            oldGoalTime = goalTime
    
    output += "Case #" + str(case) + ": " + str(time) + "\n"

with open('B-large-OUT.out', 'w') as f:
    f.write(output)

print("Done.")
