import sys

str_path="C:/Users/Ricky/Documents/1_CUNY_Queens_College/Courses/2014/Spring2014/CS780_AdvancedProgrammngTechniques/GoogleCodeJam/Q_Round/A-small-attempt1.in"

with open(str_path) as f:
    test_cases = int(f.readline())
##    print test_case
    for test_case in range(test_cases):
        cards_arrangement, new_cards_arrangement = [], []
        output = ''
        count = 0
        initial_row = int(f.readline())
        for line in range(0, 4):
            input = f.readline().split()
            cards_arrangement.append(input)
##        print cards_arrangement
        final_row = int(f.readline())
        for line in range(0, 4):
            input = f.readline().split()
            new_cards_arrangement.append(input)
##        print new_cards_arrangement

        for i in cards_arrangement[initial_row-1]:
            for j in new_cards_arrangement[final_row-1]:
                if i == j:
                    count += 1
                    output = i
        if count == 0:
            output = "Volunteer cheated!"
        elif count > 1:
            output = "Bad magician!"
        #http://stackoverflow.com/questions/255147/how-do-i-keep-python-print-from-adding-spaces
        sys.stdout.write('Case #')
        sys.stdout.write(str(test_case+1))
        sys.stdout.write(': ')
        print output
