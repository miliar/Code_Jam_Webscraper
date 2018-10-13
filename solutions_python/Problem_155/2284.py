def standingOvation(inString):
    friends = 0
    totalMembers = 0
    dataset = inString.split(' ')
    largest = int(dataset[0])
    peopleString = dataset[1]
    for i in range(largest):
        totalMembers += int(peopleString[i])
        nextNumber = i + 1
        while totalMembers < nextNumber and int(peopleString[i + 1]) > 0:
            friends += 1
            totalMembers += 1

    return friends

def main():
    infile = open("in", mode='r')
    outfile = open("out", mode='w')
    count = int(infile.readline().rstrip('\n'))
    for i in range(count):
        inputString = infile.readline().rstrip('\n')
        print("Case #"+ str(i + 1) + ":", end=" ")
        print("Case #"+ str(i + 1) + ":", end=" ", file=outfile)
        print(standingOvation(inputString))
        print(standingOvation(inputString), file=outfile)

if __name__ == "__main__" :
    main()
