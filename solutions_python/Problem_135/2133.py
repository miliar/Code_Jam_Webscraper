import fileinput

# L - Length of words in the alien language
# D - Number of words in the alien language
# N - Number of test cases

infile = fileinput.input()

T = int(infile.readline())

for X in range(1, T+1):
    answer1 = int(infile.readline()) - 1

    b1 = []
    
    for row in range(4):
        b1.append(infile.readline().strip().split())

    #print(b1)

    answer2 = int(infile.readline()) - 1

    b2 = []
    for row in range(4):
        b2.append(infile.readline().strip().split())

    #print(b2)

    matchingList = list()
    for i in b1[answer1]:
        for j in b2[answer2]:
            if i == j:
                matchingList.append(i)

    result = ""

    if len(matchingList) > 1:
        result = "Bad magician!"
    elif len(matchingList) == 0:
        result = "Volunteer cheated!"
    else:
        result = matchingList[0]

    print("Case #", X, ": ", result, sep='')

    
