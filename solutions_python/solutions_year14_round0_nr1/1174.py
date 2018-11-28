import sys

test_cases = int(input())
case = 1
for test in range(test_cases):
    print("Case #",end="")
    print(case, end="")
    row1 = int(input())-1
    arrange1 = []
    for i in range(4):
        arrange1.append(map(int, input().split()))
    arrange2 = []
    row2 = int(input())-1
    for i in range(4):
        arrange2.append(map(int, input().split()))
    res = set(arrange1[row1])&set(arrange2[row2])
    if not res:
        print(": Volunteer cheated!")
    elif len(res) == 1:
        for j in res:
            print(":",j)
    elif len(res) > 1:
        print(": Bad magician!")
    case = case + 1






