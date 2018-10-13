import sys
from math import sqrt, floor, ceil
from numpy import transpose


def result(lst):
    if len(lst) == 0:
        return "Volunteer cheated!"
    elif len(lst)>1:
        return "Bad magician!"
    else:
        return str(lst[0])

def solve(ans1, table1, ans2, table2):
    possible_answers1 = table1[ans1-1]
    possible_answers2 = table2[ans2-1]
    answer = []
    for value in possible_answers1:
        if value in possible_answers2:
            answer.append(value)
    return result(answer)

file = sys.argv[1]
with open(file) as input:
    with open("output.txt", "w") as output:
        numcases = int(input.readline())
        for casenum in range(1,numcases+1):

            ans1 = int(input.readline())
            table1 = []
            for i in range(0,4):
                line = list(map(int, input.readline().split()))
                table1.append(line)
            ans2 = int(input.readline())
            table2 = []
            for i in range(0,4):
                line = list(map(int, input.readline().split()))
                table2.append(line)
            msg = "Case #{0}: {1}\n".format(str(casenum), solve(ans1,table1,ans2,table2))
            output.write(msg)
