import sys

def isAscending(list):
    previous = list[0]
    for number in list:
        if number < previous:
            return False
        previous = number
    return True

i=0
with open("B-small-attempt0.in") as f:
    for line in f:

        tidy = False
        n = int(line)
        while(not tidy):
            if isAscending(list(map(int, list(str(n))))):
                print("Case #" + str(i) + ": " + str(n))
                tidy=True
            else:
                n-=1
        i+=1
