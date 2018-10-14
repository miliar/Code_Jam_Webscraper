def timeWithByingFarms(farms, farm_cost, farm_bonus, goal):
    total_time = 0
    farms_bought = 0
    bonus = 2 + farm_bonus * farms_bought
    for i in range(farms):
        total_time += farm_cost / bonus
        bonus += farm_bonus
    total_time += goal / bonus
    return total_time


fin = open("input.txt", 'r')
fout = open("output.txt", 'w')
c = int(fin.readline())
for i in range(c):
    farm_cost, farm_bonus, goal = map(float, fin.readline().split())
    if farm_cost >= goal:
        ans = goal / 2.0
    else:
        bought_farms = 0
        while timeWithByingFarms(bought_farms, farm_cost, farm_bonus, goal) > timeWithByingFarms(bought_farms + 1, farm_cost, farm_bonus, goal):
            bought_farms += 1
        ans = timeWithByingFarms(bought_farms, farm_cost, farm_bonus, goal)
    fout.write("Case #" + str(i + 1) + ": " + str(ans) + "\n")
fin.close()
fout.close()

