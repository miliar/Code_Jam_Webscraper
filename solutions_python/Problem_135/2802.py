class ProblemA:
    answer = ''
    matches = 0
    output = ''

    with open("E:\\file.txt") as f:
        content = f.readlines()

        i = content.pop(0)
        for x in range(1, int(i)+1):
            firstGuess = content.pop(0)
            values1 = content[int(firstGuess)-1].split()
            del content[0:4]
            secondGuess = content.pop(0)
            values2 = content[int(secondGuess)-1].split()
            del content[0:4]

            for v1 in values1:
                for v2 in values2:
                    if v1 == v2:
                        answer = v1
                        matches += 1
            output += 'Case #%s: ' % x
            if matches == 0:
                output += 'Volunteer cheated!\n'
            if matches == 1:
                output += answer + '\n'
            if matches > 1:
                output += 'Bad magician!\n'

            matches = 0

    text_file = open("E:\\output.txt", "w")
    text_file.write(output)
    text_file.close

    pass