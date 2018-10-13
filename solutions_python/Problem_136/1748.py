f = open("B-small-attempt0.in", "r+")
output = open("output.txt", "w")

num_cases = int(f.readline())

for case_num in range(0, num_cases):
    farm_cost, farm_bonus, goal = [float(i) for i in f.readline().split(" ")]

    best_time = 10000000000
    current_time = 0
    farm_count = 0
    try_again = True
    
    while try_again:
        current_time = 0
        income = 2
        for i in range(0, farm_count):
            current_time += (farm_cost / income)
            income += farm_bonus
        current_time += (goal / income)

        if current_time <= best_time:
            best_time = current_time
            try_again = True
            farm_count += 1
        else:
            try_again = False

    output.write("Case #" + str(case_num + 1) + ": " + str(best_time) + "\n")

f.close()
output.close()
