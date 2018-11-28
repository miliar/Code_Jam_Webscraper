testCases = int(input())
cases = []
for i in range(testCases):
    cases.append(input())

for i in range(len(cases)):
    case = cases[i]
    line = case.split(" ")
    num = 0
    total = 0
    people = str(line[1].split(" "))
    people = people.split("'")

    j = 0
    for number in people[1]:
        while total < j:
            total += 1
            num += 1
        total += int(number)
        j += 1
    print("Case #{}: {}".format(i+1, num))
        
