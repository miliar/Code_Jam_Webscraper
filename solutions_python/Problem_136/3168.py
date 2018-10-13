f = open('B-large.in', 'r')

output = ""


amountCases = int(f.readline())

for caseNumber in range(amountCases):
    numbers = f.readline().split()
    cost = float(numbers[0])
    extra = float(numbers[1])
    goal = float(numbers[2])
    cookies = 0
    speed = 2
    time = 0
    goOn = True
    if goal < cost:
        time = goal/speed
        goOn = False
    else:
        cookies += cost
        time = cost/speed
    while goOn:
        criticalPoint = cookies + cost/extra*speed
        if goal > criticalPoint:
            cookies += -cost + cost
            speed += extra
            time += cost/speed
        else:
            time += (goal - cookies)/speed
            goOn = False

    

    output += "Case #" + str(caseNumber+1) + ": " + str(time) + "\n"

f.close()

f = open('result.out', 'w')
f.write(output)
f.close()


