file = open('A-small-attempt0.in', 'r')
input = file.readlines()
file.close()

output = []

for i in range(int(input[0])):
  possible_answers = []

  first_answer = int(input[(i*10) + 1])
  first_order = []
  first_order.append([int(x) for x in input[(i*10) + 2].split(' ')])
  first_order.append([int(x) for x in input[(i*10) + 3].split(' ')])
  first_order.append([int(x) for x in input[(i*10) + 4].split(' ')])
  first_order.append([int(x) for x in input[(i*10) + 5].split(' ')])

  possible_answers.append(first_order[first_answer - 1])

  second_answer = int(input[(i*10) + 6])
  second_order = []
  second_order.append([int(x) for x in input[(i*10) + 7].split(' ')])
  second_order.append([int(x) for x in input[(i*10) + 8].split(' ')])
  second_order.append([int(x) for x in input[(i*10) + 9].split(' ')])
  second_order.append([int(x) for x in input[(i*10) + 10].split(' ')])

  possible_answers.append(second_order[second_answer - 1])

  answer = -1
  for x in possible_answers[0]:
    if x in possible_answers[1]:
      if answer == -1:
        answer = x
      else:
        answer = -2
        break
  if answer == -1:
    output.append('Case #%d: %s' % (i + 1, 'Volunteer cheated!'))
  elif answer == -2:
    output.append('Case #%d: %s' % (i + 1, 'Bad magician!'))
  else:
    output.append('Case #%d: %d' % (i + 1, answer))

print "\n".join(output)
