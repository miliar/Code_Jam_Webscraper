from math import ceil

file = open("C:\CodeJam\\QualificationBsmall.in","r")
output = open("C:\CodeJam\\QualificationBsmall.txt","w")

cases = int(file.readline())

for case in range(1,cases+1):
    caseText = file.readline()
    numbers = list(map(int,caseText.split()))
    googlers, surprising, requirement, scores = numbers[0], numbers[1], numbers[2], numbers[3:]
    total = 0
    almost = 0
    for score in scores:
        if ceil(score / 3.0) >= requirement:
            total += 1
        elif score > 2 and ceil(score / 3.0) + 1 >= requirement and score % 3 != 1:
            almost += 1
    total += min(almost,surprising)
    output.write("Case #" + str(case) + ": " + str(total))
    if case != cases:
        output.write("\n")

file.close()
output.close()