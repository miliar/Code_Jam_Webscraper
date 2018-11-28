# Code Jam 2016 Qual
# Nikhil Phatak


def isTidy(n):
    string = str(n)
    for i in range(1, len(string)):
        if int(string[i - 1]) > int(string[i]):
            return False
    
    return True


def highestTidy(n):
    for i in range(int(n), 0, -1):
        if isTidy(i):
            return i

t = int(input())
for i in range(1, t + 1):
  n = input()  # read a list of integers, 2 in this case
  print("Case #{}: {}".format(i, highestTidy(n)))
