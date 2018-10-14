# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
from numpy import prod
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    N, K = [int(s) for s in input().strip().split()]
    U = int(input().strip().replace('.', ''))
    listOfProba = [int(s) for s in input().strip().replace('.', '').split()]  # read a list of integers, 2 in this case
    listOfProba = sorted(listOfProba)
    newList = [0]
    j = 0
    for proba in (listOfProba[1:]+[10000]):
        j += 1
        newList.append(newList[-1] + j * (proba - listOfProba[j-1]))
    j = 0
    for j in range(N):
        if U < newList[j]:
            break
        j += 1
    for k in range(j):
        listOfProba[k] = listOfProba[j-1] + (U - newList[j-1])/j
    listOfProba = list(map(lambda x : x/10000, listOfProba))
    print("Case #%s: %.6f" % (i, prod(listOfProba)))
    # check out .format's specification for more formatting options
