# compare the digits in num
def tidy(numList):
    for sth in range(len(numList)-1):
        if int(numList[sth]) > int(numList[sth+1]):
            sum = 0
            for num in numList[:sth+2]:
                sum = sum*10 + int(num)
            sum -= 1
            numList = [int(char) for char in str(sum)] + [9]*(len(numList)-(sth+2))
            return numList
    return numList

#combine array into number
def magic(numList):
    s = ''.join(map(str, numList))
    return s

#reading the file
fvar = open('B-large.in', 'r')

data = [line.rstrip() for line in fvar.readlines()]
testcases = data[0]
alldatestcases = data[1:]

c = 1
for case in alldatestcases:
    numList = [int(x) for x in str(case)]
    if int(case) < 20 and not case == "10":
        print ('Case #' + str(c) + ': ' + case)
    else:
        while not numList == tidy(numList):
            numList = tidy(numList)
        print('Case #' + str(c) + ': ' + str(magic(numList)))
    c += 1



