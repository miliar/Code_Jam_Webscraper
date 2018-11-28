file = open("C:\CodeJam\\Round1AALarge.in","r")
output = open("C:\CodeJam\\Round1AAlarge.txt","w")

cases = int(file.readline())

for case in range(1,cases+1):
    caseText = file.readline().strip().split()

    maximumGamesToday = int(caseText.pop(0))
    percentageToday = int(caseText.pop(0))
    percentageTotal = int(caseText.pop(0))

    if (percentageTotal == 0 and percentageToday != 0) or (percentageTotal == 100 and percentageToday != 100):
        output.write("Case #"+str(case)+": "+"Broken")
        if case != cases:
            output.write("\n")
        continue

    result = "Broken"
    for gamesToday in range(1, maximumGamesToday+1):
        gamesWonToday = gamesToday*float(percentageToday)/100
        if gamesWonToday % 1 == 0:
            result = "Possible"
            break

    output.write("Case #"+str(case)+": "+result)
    if case != cases:
        output.write("\n")

output.close()