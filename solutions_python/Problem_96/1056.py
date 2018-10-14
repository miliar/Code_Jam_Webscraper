def dancing(scores, p, simlar):
  number_above_p = 0
  for score in scores:
    score = int(score)
    mod_score = score % 3
    if (mod_score == 1):
      if ((((score - 1) / 3) + 1) >= p):
        number_above_p += 1

    if (mod_score == 0):
      if ((score / 3) >= p):
        number_above_p += 1
      else:
        if (((score / 3) + 1) >= p):
          if not (score == 0):
            if (simlar > 0):
              simlar -= 1
              number_above_p += 1

    if (mod_score == 2):
      if ((((score - 2) / 3) + 1) >= p):
        number_above_p += 1
      else:
        if ((((score - 2) / 3) + 2) >= p):
          if (simlar > 0):
            simlar -= 1
            number_above_p += 1
  return number_above_p

def solve(input_line):
  split_input = input_line.split(" ")
  p = int(split_input[2])
  s = int(split_input[1])
  n = int(split_input[0])
  scores = list()
  for i in range(n):
    scores.append(int(split_input[i+3]))
  return dancing(scores,p,s)

def process_tests(command_to_run):
    in_file = open('in')
    out_file = open("out","w")
    number_of_tests = int(in_file.readline())
    for test_case in range(number_of_tests):
        test_string = in_file.readline()[:-1]
        test_answer = command_to_run(test_string)
        out_file.write("Case #" + str(test_case + 1) + ": " + str(test_answer) + "\n")
    out_file.close()
    in_file.close()

process_tests(solve)
