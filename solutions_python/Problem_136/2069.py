import fileinput

def stringListToRealList(stringList):
    result = list()
    for number in stringList:
        result.append(float(number))

    return result

# L - Length of words in the alien language
# D - Number of words in the alien language
# N - Number of test cases

infile = fileinput.input()

T = int(infile.readline())

for i in range(1, T+1):
    C, F, X = stringListToRealList(infile.readline().strip().split())

    result = -1.0
    accumTime = 0.0
    rate = 2
    
    while result < 0:
        slowTime = X / rate
        timeToBuy = C / rate
        timeWithFarm = (X / (rate + F)) + timeToBuy

        if slowTime < timeWithFarm:
            result = slowTime + accumTime
            
        rate += F
        accumTime += timeToBuy

    print("Case #", i, ": ", result, sep='')
