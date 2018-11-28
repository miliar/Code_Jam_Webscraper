with open('dancing_with_the_googlers.txt') as f :
    lines = f.readlines()

num_cases = int(lines[0])

for i in range(num_cases) :
    line = lines[i+1].split(' ')
    googlers = int(line[0])
    special_cases = int(line[1])
    score = int(line[2])
    accepted = 0
    for g in range(googlers) :
        total = int(line[g+3])
        if (score == 0) :
            accepted = accepted + 1
        elif (score == 1) :
            if (total != 0) :
                accepted = accepted + 1
        else :
            if (total > (3*score - 3)) :
                accepted = accepted + 1
            elif (total > (3*score - 5)) :
                if (special_cases > 0) :
                    special_cases = special_cases - 1
                    accepted = accepted + 1
    with open('dancing_with_the_googlers_o.txt', 'a') as f :
        f.write('Case #' + str(i+1) + ': ' + str(accepted) + '\n')
