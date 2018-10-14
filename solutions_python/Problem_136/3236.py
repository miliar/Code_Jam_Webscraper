# R: rate of cookiers per second
# P: time spent purchasing farms

def cookie_clicker(C, F, X):
  R, P = 2, 0
  while True:
    time_at_current_rate = X/R + P
    time_with_new_farm = X/(R+F) + (C/R) + P
    if time_at_current_rate <= time_with_new_farm:
      return time_at_current_rate
    else:
      R, P = R+F, P+(C/R)

def cookie_clicker_test(input_path, output_path):
  file = open(input_path,'r')
  open(output_path, 'w').close()
  number_tests, test = int(next(file)), 1
  while test <= number_tests:
    inputs = list(map(float, next(file).split(" ")))
    with open(output_path, "a") as text_file:
      text_file.write("Case #"+str(test)+": ")
      text_file.write(str(cookie_clicker(inputs[0], inputs[1], inputs[2]))+"\n")
    test += 1

cookie_clicker_test("input.in", "output.in")