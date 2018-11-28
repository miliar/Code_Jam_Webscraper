input = open("input.txt").readlines()
output = open("output.txt", "w")
for i in range(len(input)):
    if input[i][-1] == '\n':
        input[i] = input[i][:-1]

nOfCases = int(input[0])
cursor = 1

for casecount in range(nOfCases):
    P,K,L = [int(i) for i in input[cursor].split()]
    list = [int(i) for i in input[cursor+1].split()]
    list.sort(reverse = True)
    cursor += 2
    
    times = 1
    result = 0
    while(len(list) > 0):
        temp = list[:K]
        sum = 0
        for i in temp:
            sum += i
        result += sum * times
        print result
        list = list[K:]
        times = times+1
    
    result = str(result)
    print >> output, "Case #" + str(casecount+1) + ": " + result
    print "Case #" + str(casecount+1) + ": "+ result
