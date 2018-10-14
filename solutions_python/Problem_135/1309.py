def getBoard(input):
    board = []
    for i in xrange(4):
        line = input.readline().strip().split(' ')
        line = [int(x) for x in line]
        board += [line]
    return board

def ans(options1, options2):
    count = 0
    res = -1
    for i in xrange(4):
        for j in xrange(4):
            if(options1[i] == options2[j]):
                count += 1
                res = options1[i]
    if(count == 1):
        return str(res)
    if(count > 1):
        return 'Bad magician!'

    return 'Volunteer cheated!'

def main():
    input = open('input.txt', 'r')
    output = open('output.txt', 'w')

    T = int(input.readline())
    for casenum in xrange(1, T + 1):
        participant_choice = int(input.readline())
        options1 = getBoard(input)[participant_choice - 1]
        participant_choice = int(input.readline())
        options2 = getBoard(input)[participant_choice - 1]

        output.write('Case #' + str(casenum) + ': ')
        output.write(ans(options1, options2))
        output.write('\n')

    input.close()
    output.close()

main()