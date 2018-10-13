def main():
  print "Magician Algorithm"
  print "Please enter the input file name"
  file_name = raw_input()

  with open(file_name, 'r') as f:
    with open('output.txt', 'w') as output:
      t = int(f.readline()) # Test cases

      test_case_size = 10

      for i in range(t):
        test_case = []

        for j in range(test_case_size):
          test_case.append(f.readline())

        result = solve(test_case)
        output.write("Case #" + str(i + 1) + ": " + result + "\n")

def solve(test_case):
  m = int(test_case[0])
  n = int(test_case[5])

  answers = []
  first_row = test_case[m].split()
  second_row = test_case[5 + n].split()

  for x in first_row:
    if x in second_row:
      answers.append(x)

  if len(answers) == 0:
    return "Volunteer cheated!"
  elif len(answers) > 1:
    return "Bad magician!"
  else:
    return answers[0]

main()