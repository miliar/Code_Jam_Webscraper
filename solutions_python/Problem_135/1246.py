sol = []
for case in range(int(raw_input())):
    x = int(raw_input())
    rows1 = [map(int, raw_input().split()) for i in range(4)]

    y = int(raw_input())
    rows2 = [map(int, raw_input().split()) for i in range(4)]

    count = 0
    number = 0
    for i in range(4):
        temp = rows1[x-1][i]
        for j in range(4):
            if temp == rows2[y-1][j]:
                count += 1
                number = temp

    if count == 1:
        sol.append("Case #" + str(case + 1) + ": " + str(number))
    elif count == 0:
        sol.append("Case #" + str(case + 1) + ": " +  "Volunteer cheated!")
    else:
        sol.append("Case #" + str(case + 1) + ": " + "Bad magician!")

for i in sol:
    print i