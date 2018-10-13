# Guillermo Ortas

# dataFile = open("Q_B.txt", 'r')
dataFile = open("B-large.in", 'r')
target = open("output.out", 'w+')

rows = int(dataFile.readline())

m = 1
for line in dataFile:
    number = int(line)
    number = list(str(number))

    tidy = 0
    while not tidy:
        tidy = 1
        for i in range(len(number)-1):
            if number[i] > number[i+1]:
                tidy = 0
                number[i] = str(int(number[i])-1 % 10)
                for j in range(i+1, len(number)):
                    number[j] = "9"

    # for i in range(len(number)):
    #     for i in range(len(number)-1):
    #         if number[i] > number[i+1]:
    #             tidy = 0
    #             number[i] = str(int(number[i])-1 % 10)
    #             for j in range(i+1, len(number)):
    #                 number[j] = "9"

    number = int("".join(number))
    # print number
    target.write("Case #" + str(m) + ": " + str(number) + "\n")
    m += 1


target.close()