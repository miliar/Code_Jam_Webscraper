def flip(row, flipperSize, idx):
    for i in range(flipperSize):
        row[idx + i] = flipElement(row[idx + i])

def flipElement(actual):
    if actual == "+":
        return "-"
    else:
        return "+"

def solved(row):
    if "-" not in row:
        return True
    else:
        return False


def answer(row, flipperSize):
    row = list(row)
    times = 0
    size = len(row)

    # already done
    if solved(row): 
        return 0
    
    for i in range(size - flipperSize + 1):
        if (row[i] == '-'):
            flip(row, flipperSize, i)
            times += 1

    if solved(row):
        return times
    else:
        return "IMPOSSIBLE"



times = int(input())  # read a line with a single integer
for i in range(1, times + 1):
  row, flipperSize = input().split(" ")  # read a list of integer
  flipperSize = int(flipperSize)

  print("Case #" + str(i) + ": " + str(answer(row, flipperSize)))