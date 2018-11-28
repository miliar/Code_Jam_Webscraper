
def LoadInput():

   with open("input.txt") as f:
      return f.read()
   
def Output(text):

   with open("output.txt", "w") as f:
      f.write(text)

def ParseInput(text):

    text = text.split('\n')

    lines = int(text.pop(0))

    cases = []

    while lines:
        lines -= 1
        R, K, N = map(int, text.pop(0).split())
        groups = map(int, text.pop(0).split())
        cases += [ [ R, K, groups ] ]
        

    return cases

#figure out how many groups can fit and the cost starting
#with a particular group
def FigureGroupData(i, groups, k):

    groups = groups[i:] + groups[:i]

    groupsFitCount = 0
    profit = 0

    for group in groups:

        if profit + group <= k:
            groupsFitCount += 1
            profit += group
        else:
            break

    return groupsFitCount, profit
    

def DoTestCase(case):

    R, k, groups = case

    groupCount = len(groups)


    groupData = []

    for i, group in enumerate(groups):

        groupData += [ FigureGroupData(i, groups, k) ]

    groupIndex = 0
    result = 0

    while R:
        R -= 1

        result += groupData[groupIndex][1]
        
        groupIndex = (groupIndex + groupData[groupIndex][0]) % groupCount
    
    return result
    

def main():

    testCases = ParseInput(LoadInput())

    result = []
    
    for i, case in enumerate(testCases):
        result.append("Case #{0}: {1}".format(i + 1, DoTestCase(case)))

    result = '\n'.join(result)

    Output(result)
    print "done, result:"
    print result


    

if __name__ == "__main__":

    main()
