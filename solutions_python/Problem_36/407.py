def count_occurences(target, string):
    if len(target) == 0:
        return 1

    #find indexes of target[0] in string
    indexes = []
    index = string.find(target[0])
    while index != -1:
        indexes.append(index)
        index = string.find(target[0], index + 1)

    count = 0
    for index in indexes:
        count = (count + count_occurences(target[1:],
                    string[index + 1:])) % 10000

    return count


INPUT = open('C-small-attempt0.in')
N = int(INPUT.readline().strip())

OUTPUT = open('C-small-attempt0.out', 'w')
for i in range(N):
    string = INPUT.readline().strip()
    count = str(count_occurences('welcome to code jam', string))
    for j in range(4 - len(count)):
        count = '0' + count

    print >> OUTPUT, "Case #" + str(i + 1) + ": " + count

OUTPUT.close()
INPUT.close()
