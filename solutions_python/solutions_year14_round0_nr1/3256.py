f = open('A-small-attempt0.in', 'r')

output = ""
result = []

amountCases = int(f.readline())

for caseNumber in range(amountCases):
    for i in range(2):
        row = int(f.readline())
        for j in range(4):
            if j == row-1:
                if i == 0:
                    possibleCards = f.readline().split()
                elif i == 1:
                    amountSolutions = 0 
                    for candidate in f.readline().split():
                        if candidate in possibleCards:
                            amountSolutions += 1
                            solution = candidate
            else:
                f.readline()

    

    output += "Case #" + str(caseNumber+1) + ": "
    if amountSolutions == 0:
        output += "Volunteer cheated!\n"
    elif amountSolutions == 1:
        output += str(solution) + "\n"    
    elif amountSolutions > 1:
        output += "Bad Magician!\n"    


f.close()
f = open('result.out', 'w')
f.write(output)
f.close()


