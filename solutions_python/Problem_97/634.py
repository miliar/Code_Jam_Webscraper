
def fullcycle(inputNum):
    indexes = range(1,len(str(inputNum)))
    allcycles = []
    for rot in indexes:
        allcycles.append( cycle(inputNum,rot))
    return allcycles

def cycle(inval, howfar):
    num_as_str = str(inval)
    front = num_as_str[:howfar]
    num_as_str = num_as_str[howfar:]
    return int(num_as_str + front)

def findRecycledNums(fromA,toB):
    matchingPairs = []
    en = fromA
    while (en < toB):
        recycledNums = fullcycle(en)
        matches = [(en,em) for em in recycledNums
                   if em <= toB and en < em]
        matchingPairs.extend(matches)
        en += 1
    #print "before set, matching pairs length was: " + str(matchingPairs)
    return set(matchingPairs)  # set probably not needed but shouldn't hurt

def findRecycleNumCount(fromA,toB):
    fromA = int(fromA)
    toB = int(toB)
    return len(findRecycledNums(fromA, toB))

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        filename = "input.in"
    else:
        filename = sys.argv[1]

    read_file = file(filename)
    file_contents = list(read_file.readlines())
    del file_contents[0] # skip first line of input since it's just the number of test cases

    counter = 1
    for line in file_contents:
        line = line[:-1]  # chop off end-of-line
        fromA, toB = line.split()
        print "Case #" + str(counter) + ": " + str(findRecycleNumCount(fromA,toB))

        counter += 1

