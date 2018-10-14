def solve_magic_trick(row_1, row_2):
  number_solutions = 0
  for i in range(0, 4):
    for j in range(0, 4):
      if row_1[i] == row_2[j]:
        if number_solutions == 0: solution = row_1[i]
        number_solutions += 1
  if number_solutions == 0:
    return "Volunteer cheated!"
  elif number_solutions == 1:
    return str(solution)
  else:
    return "Bad magician!"

def magic_trick(input_path, output_path):
  file = open(input_path,'r')
  open(output_path, 'w').close()
  number_tests, test = int(next(file)), 1
  while test <= number_tests:
    answer_1 = int(next(file))
    arrangement_1, arrangement_2 = [], []
    for _ in range(4): arrangement_1.append(list(map(int, next(file).split(" "))))
    answer_2 = int(next(file))
    for _ in range(4): arrangement_2.append(list(map(int, next(file).split(" "))))
    with open(output_path, "a") as text_file:
      text_file.write("Case #"+str(test)+": ")
      text_file.write(solve_magic_trick(arrangement_1[answer_1-1], arrangement_2[answer_2-1])+"\n")
    test += 1

magic_trick("input.in", "output.in")