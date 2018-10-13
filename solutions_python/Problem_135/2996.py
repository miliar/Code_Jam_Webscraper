
def game():
  lines = []
  answer = int(raw_input())
  for i in xrange(0,4):
    lines.append(raw_input())
  return lines[answer-1]

def what_is_equal(first, second):
  should_return = []
  for i in first.split(' '):
    for j in second.split(' '):
      if j == i and i != ' ':
        should_return.append(j)

  if len(should_return) == 1:
    return should_return[0]
  elif len(should_return) > 1:
    return 'Bad magician!'
  else:
    return 'Volunteer cheated!'

  return 'bad bad game'

if __name__ == '__main__':
  number_of_cases = int(raw_input())
  for i in xrange(0,number_of_cases):
    answers = []
    for j in xrange(0,2):
      answers.append(game())

    print "Case #" +str(i+1)+": " + str(what_is_equal(answers[0], answers[1]))
