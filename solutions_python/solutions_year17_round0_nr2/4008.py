def isNonDec(s) :
    for i in range(1, len(s)) :
        if s[i - 1] > s[i] :
            return False;
    return True

infile = open("B-small-attempt0.in", "r")
outfile = open("test.out", "w")

t = int(infile.readline())

for i in range(t) :
    num = int(infile.readline())
    while not isNonDec(str(num)) :
        num -= (num % pow(10, len(str(num)) - 2) + 1)
    outfile.write('Case #' + str(i + 1) + ': ' +str(num) + '\n')
    print('Case #' + str(i + 1) + ': ' +str(num))

infile.close()
outfile.close()
