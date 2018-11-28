input_file = open('A-large.in')
lines = (line for line in input_file)

case_numbers = (str(n) for n in range(1,int(lines.__next__())+1))
with open('output-large.out', 'w') as out:
    for line in lines:
        highest_shy_level, cohorts = line.split()

        number_of_friends = 0
        threshold = 0
        for i, c in enumerate(cohorts):
            if c == '0' and threshold < i+1:
                number_of_friends +=1
                threshold +=1
            else:
                threshold += int(c)
            if threshold >= int(highest_shy_level):
                break

        out.write('Case #' + case_numbers.__next__() + ': ' \
                           + str(number_of_friends)+"\n")

