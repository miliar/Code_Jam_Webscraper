file_name = 'A-small-attempt0.in'

with open(file_name, 'r') as infile:
    cases = int(infile.readline())
    for case in range(1, cases+1):

        volunteers_rows = list()
        for x in range(2):
            volunteers_row = int(infile.readline()) - 1 #-1 because it's not zero indexed
            cards = [] #2d arrray of the current card configuration
            for x in range(4):
                row = [int(num) for num in infile.readline().split(' ')]
                cards.append(set(row))
            volunteers_rows.append(set(cards[volunteers_row]))

        possible_nums = volunteers_rows[0] & volunteers_rows[1] #all the elements that are within both rows
        possible_choices = len(possible_nums)

        output_string = 'Case #%d: ' % (case)
        if  possible_choices == 0:
            output_string += 'Volunteer cheated!'
        elif possible_choices == 1:
            output_string += str(list(possible_nums)[0])
        else:
            output_string += 'Bad magician!'
        print output_string




