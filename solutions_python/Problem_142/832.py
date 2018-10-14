import fileinput, re

def main():

  text_input = fileinput.input()

  #num of test cases
  num = int(text_input.readline())

  for case in range(num):

    string_num = int(text_input.readline())

    strings = []

    for i in range(string_num):
      strings.append(text_input.readline().rstrip())

    characters = []



    for num, i in enumerate(strings):
      characters.append([])
      count = 0
      prev = i[0]
      for j in i:
        if j != prev:
          characters[num].append([prev, count])
          prev = j
          count = 1
        else:
          count+=1
      characters[num].append([prev, count])


    get_result(characters, string_num, case)


def get_result(characters, string_num, case):

  # Check if not the same length
  length = len(characters[0])
  for i in range(1, string_num):
    if len(characters[i]) != length:
      print("Case #{0}: {1}".format(case+1, "Fegla Won"))
      return

  swaps = 0

  for i in range(length):
    swaps_required = [characters[0][i][1]]
    letter = characters[0][i][0]
    for j in range(1, string_num):
      if characters[j][i][0] != letter:
        print("Case #{0}: {1}".format(case+1, "Fegla Won"))
        return
      swaps_required.append(characters[j][i][1])
    goal = sum(swaps_required)/len(swaps_required)

    for i in swaps_required:
      swaps += abs(goal-i)

  print("Case #{0}: {1}".format(case+1, swaps))

if __name__ == "__main__":
  main()
