
def runCase(data):
    counter = 0
    max_missing = 0
    for i in range(len(data)):
        if i > counter:
            if max_missing < i - counter:
                max_missing = i - counter
        counter += data[i]
    return(str(max_missing))
            
        
f = open('A-large.in', 'r')
output = ""

amountCases = int(f.readline())

for caseNumber in range(amountCases):
    print(caseNumber)
    n_data = [i for i in f.readline().split()]
    n = int(n_data[0])
    data = n_data[1]
    data = [int(i) for i in n_data[1]]
    result = runCase(data)

    output += "Case #" + str(caseNumber+1) + ": " + result + "\n"

        
print(output)

