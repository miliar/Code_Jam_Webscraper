def isTidyNumber(number):
    while number > 0:
        last = number % 10
        prelast = (number / 10) % 10
        if last < prelast:
            return False
        number = (number / 10)
    return True

def findTidyNumber(limit): # limit should be int here
    while limit > 0:
        found = 0

        # if limit has one digit return, else check if its tidy
        if len(str(limit)) == 1 or isTidyNumber(limit):
            return limit

        # split limit in array of STRINGS
        limitArray = [t for t in str(limit)]

        # find exception index (in python string is comparable already NONSTATIC MWAHAHA)
        for index, number in enumerate(limitArray[:len(limitArray)-1]):
            if limitArray[index + 1] > number:
                found = index + 1
                break

        # decrease current item by 1
        limitArray[found] = str(int(limitArray[found]) - 1)

        # make all the rest (after exception) 9
        for index, number in enumerate(limitArray):
            if index > found:
                limitArray[index] = "9"

        # remove leading zeros(casting to int in python removes leading zeros)
        limit = int("".join(limitArray))

def solve(fname):
    with open(fname) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    content = content[1:]
    index = 0

    for t in content:
        index += 1
        print "Case #%d: %d"%(index, findTidyNumber(int(t)))


solve("sample.txt")
