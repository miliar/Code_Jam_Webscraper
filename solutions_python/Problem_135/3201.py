__author__ = 'eldos'

testCases = int(input())

for i in range(testCases):
    rows1 = []
    rows2 = []
    count = 0
    selectedRow = int(input())
    for j in range(4):
        rows1.append(input().split())
    selectedRow2 = int(input())
    for j in range(4):
        rows2.append(input().split())
    for x in rows1[selectedRow-1]:
        if x in rows2[selectedRow2 - 1]:
            count += 1
            selected = x
    if count == 0:
        print("Case #" + str(i+1) + ": Volunteer cheated!")
    elif count == 1:
        print("Case #" + str(i+1) + ": " + selected)
    else:
        print("Case #" + str(i+1) + ": Bad magician!")

