open('output.in','w').close()

with open('input.in') as file:
    lines = file.readlines()
    line = 0
    T = int(lines[line])
    for t in range(T):
        result = ''
        line += 1
        N = int(lines[line])
        strings = []
        characters = []
        reps_average = []
        first_string = lines[line+1].strip()
        for i in range(len(first_string)):
            if i == 0:
                characters.append(first_string[i])
            elif first_string[i] != first_string[i-1]:
                characters.append(first_string[i])
        for character in characters:
            reps_average.append(0)
        all_reps = []
        n = 0
        while n < N and result == '':
            line += 1
            reps_pos = 0
            reps = []
            for elem in reps_average:
                reps.append(0)
            string = lines[line].strip()
            string_characters = []
            for pos in range(len(string)):
                if pos == 0:
                    string_characters.append(string[pos])
                elif string[pos] != string[pos-1]:
                    string_characters.append(string[pos])
                elif string[pos] == string[pos-1]:
                    reps_pos += 1
                    if pos-reps_pos > len(reps):
                        result = 'Fegla Won'
                    else :
                        repeated = reps[pos-reps_pos]
                        repeated += 1
                        reps[pos-reps_pos] = repeated
            all_reps.append(reps)
            if characters != string_characters:
                result = 'Fegla Won'
            strings.append(string)
            n += 1
        line += N-n
        if result == '':
            for i in range(len(characters)):
                total = 0
                for element in all_reps:
                    total += element[i]
                average = int(round(total*1.0/len(all_reps)))
                reps_average[i] = average
            moves = 0
            for i in range(len(characters)):
                for element in all_reps:
                    moves += abs(element[i]-reps_average[i])
            result = str(moves)
        with open('output.in','rw+') as file:
            file.seek(0, 2)
            file.write('Case #'+str(t+1)+': '+result+'\n')
