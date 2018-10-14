import fileinput

def main():

  text_input = fileinput.input()

  #num of test cases
  num = text_input.readline()

  for i in range(int(num)):

    # -1 to match the way range workds
    first_guess = int(text_input.readline()) - 1

    for j in range(4):
      line = text_input.readline()
      if j == first_guess:
        first_row = set(line.rstrip().split(" "))

    second_guess = int(text_input.readline()) - 1

    for j in range(4):
      line = text_input.readline()
      if j == second_guess:
        second_row = set(line.rstrip().split(" "))

    answer = first_row.intersection(second_row)
    if len(answer) == 1:
      print ("Case #{0}: {1}".format(i+1, answer.pop()))
    elif len(answer) == 0:
      print ("Case #{0}: Volunteer cheated!".format(i+1))
    else:
      print ("Case #{0}: Bad magician!".format(i+1))

if __name__ == "__main__":
  main()
