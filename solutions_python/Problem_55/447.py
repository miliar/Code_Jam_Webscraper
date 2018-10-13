def solve(R, k, groups, case):
    out = "Case #" + str(case+1) + ": "
    profit = 0
    car = []
    while R > 0:
        occupants = 0
        while len(groups) > 0 and occupants+groups[0] <= k:
            car.append(groups.pop(0))
            occupants += car[-1]
        profit += occupants
        R -= 1
        groups += car
        car = []
    out += str(profit)
    
    return out


f = open("C-small-attempt0.in", "r")
out = ""

T = int(f.readline().strip())
for case in range(T):
    line1 = f.readline().split()
    line2 = f.readline().split()
    R = int(line1[0].strip())
    k = int(line1[1].strip())
    N = int(line1[2].strip())
    groups = []
    for i in range(N):
        groups.append(int(line2[i].strip()))
    out += solve(R, k, groups, case) + "\n"

f = open("output.txt", "w")
f.write(out)
f.close()
