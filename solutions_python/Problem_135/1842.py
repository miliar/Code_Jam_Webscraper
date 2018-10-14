

# File handles
input_file = open('A-small-attempt0.in', 'r')
output_file = open('A-small-attempt0.out', 'w')

# Function compares numbers of 
def GetCountOfSameNumbers(list1, list2):
    cntAndValue = [0, 0]
    for x in list1:
        for n in list2:
            if x == n:
                cntAndValue[0] = cntAndValue[0] + 1
                cntAndValue[1] = x

    return cntAndValue

# Function solves one game
def SolveOneGame(caseNumber):
    # Read the first question and cards
    cards1 = ReadQuestionAndCorrespondingCards()
    
    # Read the second question and cards
    cards2 = ReadQuestionAndCorrespondingCards()

    # Get the count of same numbers
    result = GetCountOfSameNumbers(cards1, cards2)

    if result[0] == 1:
        output_file.write("Case #" + str(caseNumber) + ": " + str(result[1]))
    elif result[0] > 1:
        output_file.write("Case #" + str(caseNumber) + ": Bad magician!")
    else:
        output_file.write("Case #" + str(caseNumber) + ": Volunteer cheated!")

    # Print new line
    output_file.write("\n")
 
    
  
# Function reads the row number and returns cards from that row
def ReadQuestionAndCorrespondingCards():
    numbers_list = []
    row_number = int(input_file.readline())
    for x in range(1, 5):
       line_str = input_file.readline()
       if x == row_number:
           numbers_list = line_str.split()

    return numbers_list
       

# The main logic
number_of_games = int(input_file.readline())
for g in range(0, number_of_games):
    SolveOneGame(g + 1)


# Close the files
input_file.close()
output_file.close()