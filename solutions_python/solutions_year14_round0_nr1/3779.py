#2D array of rows and than the row values
with open('A-small-attempt1.in') as f:
    number_of_cases = int(f.readline().strip())
    for case in range(1, number_of_cases+1):
        cards1 = []
        cards2 = []
        row_number1 = int(f.readline().strip())
        for i in range(4):
            row = f.readline().strip().split() #['1','2','3','4']
            cards1.append(row)
        part1Row = cards1[row_number1-1]

        row_number2 = int(f.readline().strip())
        for i in range(4):
            row = f.readline().strip().split() #['1','2','3','4']
            cards2.append(row)
        part2Row = cards2[row_number2-1]
        #compare rows for same values
        intersection = set(part1Row).intersection(set(part2Row))
        number_of_matches = len(intersection)
        if number_of_matches == 1:
            print('Case #{}: {}'.format(case, list(intersection)[0]) )
        elif number_of_matches >1:
            print('Case #{}: Bad magician!'.format(case) )
        else:
            print('Case #{}: Volunteer cheated!'.format(case))
        
        
