filename = 'file.in'

def makeInt(strlist):
    string = ''.join(strlist)
    return int(string) 


def getCycles(num):
    digits = list(str(num))
    toreturn = []
    if len(digits) == 1:
        return toreturn
    for i in range(len(digits)):
        strlist = digits[i:]
        back = digits[0:i]
        for item in back:
            strlist.append(item)
        if strlist[0] == "0":
            continue
        toreturn.append(makeInt(strlist))
    return toreturn

if __name__ == "__main__":
    with open(filename, 'r') as inputfile:
        rows = int(inputfile.readline())
        for i in range(rows):
            valid = set([])

            line = inputfile.readline()
            AB = line.split(" ")
            A = int(AB[0])
            B = int(AB[1])

            for num in range(A, B):
                for cycle in getCycles(num):
                    if cycle > num and cycle <= B:
                        valid.add((num,cycle))

            print "Case #" + str(i+1) + ": " + str(len(valid))