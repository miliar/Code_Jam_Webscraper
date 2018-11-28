f = open("A-small-attempt1.in", "r")
#number_of_case = input()
number_of_case = int(f.readline().strip())
count_case = 1
while (count_case <= number_of_case):
  answer_list = []
  #FIRST QUESTION
  #volunteer_first_answer = input()
  volunteer_first_answer = int(f.readline().strip())
  first_square_grid = []
  first_square_grid.append(f.readline().strip().split(" "))
  first_square_grid.append(f.readline().strip().split(" "))
  first_square_grid.append(f.readline().strip().split(" "))
  first_square_grid.append(f.readline().strip().split(" "))
  first_list_volunteer_selected = first_square_grid[volunteer_first_answer - 1]
  #SECOND QUESTION
  #volunteer_second_answer = input()
  volunteer_second_answer = int(f.readline().strip())
  second_square_grid = []
  second_square_grid.append(f.readline().strip().split(" "))
  second_square_grid.append(f.readline().strip().split(" "))
  second_square_grid.append(f.readline().strip().split(" "))
  second_square_grid.append(f.readline().strip().split(" "))
  second_list_volunteer_selected = second_square_grid[volunteer_second_answer - 1]
  count_number_can_selected = 0
  #print first_list_volunteer_selected
  #print second_list_volunteer_selected
  for FIRST_NUMBER in first_list_volunteer_selected:
    for SECOND_NUMBER in second_list_volunteer_selected:
      if (FIRST_NUMBER == SECOND_NUMBER):
        count_number_can_selected = count_number_can_selected + 1
        answer_list.append(FIRST_NUMBER)
  if (count_number_can_selected == 0):
    print "Case #" + str(count_case) + ": Volunteer cheated!"
  elif (count_number_can_selected == 1):
    print "Case #" + str(count_case) + ": " + answer_list[0]
  elif (count_number_can_selected > 1):
    print "Case #" + str(count_case) + ": Bad magician!"
  count_case = count_case + 1
