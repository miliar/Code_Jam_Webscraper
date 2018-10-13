import sys
from math import sqrt, floor
f = open(sys.argv[1], 'r')

numOfTest = int(f.readline())

for i in range(1, numOfTest + 1) :
    print("Case #" + str(i) + ":", end=' ')
    
    # read test case
    n = int(f.readline())
    strs = []
    for j in range(n):
        strs.append(f.readline())

    index = 0
    action = 0
    possible = True
    while True:
        if strs[0][index] == strs[1][index]:
            index += 1
            if index >= len(strs[0]) or index >= len(strs[1]):
                break
        else:
            if index == 0:
                possible = False
                break
            elif strs[0][index - 1] == strs[1][index]:
                strs[0] = strs[0][:index] + strs[1][index] + strs[0][index:]
                action += 1
            elif strs[1][index - 1] == strs[0][index]:
                strs[1] = strs[1][:index] + strs[0][index] + strs[1][index:]
                action += 1
            elif strs[0][index - 1] == strs[0][index]:
                strs[0] = strs[0][:index] + strs[0][index + 1:]
            elif strs[1][index - 1] == strs[1][index]:
                strs[1] = strs[1][:index] + strs[1][index + 1:]
            else:
                possible = False
                break
    if possible:
        print(action)
    else:
        print('Fegla Won')
