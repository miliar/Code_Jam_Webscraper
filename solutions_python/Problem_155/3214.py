with open("inA", "r") as input:
    case_num = 0
    case = 0
    start = True
    case_to_max = dict()
    case_to_data = dict()
    for line in input:
        if start == True:
            case = 1
            case_num = int(line)
            start = False
        else:
            max_need = int(line.split(' ')[0])
            data = line.split(" ")[1]
            case_to_data[case] = data
            case_to_max[case] = max_need
            case += 1

with open("outA", 'w') as output:
    for case in range(1, case_num+1):
        data = case_to_data[case]
        max = case_to_max[case]
        friends = 0
        stand = int(data[0])
        for i in range(1, max+1):
            needed = i - (friends + stand)
            if needed >0:
                friends += needed
                stand += int(data[i])
            else:
                stand += int(data[i])
        output.write("Case #"+ str(case)+": "+str(friends)+'\n')
