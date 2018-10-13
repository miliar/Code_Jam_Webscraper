file = open('B-small-attempt0.in', 'r')
input = file.readlines()
file.close()

f = open('B-small.out', 'w')

output = []

for i in range(1, int(input[0]) + 1):
  cookies = 0
  rate = 2
  time = 0
  values = [float(x) for x in input[i].split(" ")]
  C = values[0]
  F = values[1]
  X = values[2]

  outcomes = []

  x = 0
  while True:
    answer = 0
    for n in range(0, x):
      answer += C / (2 + F*n)
    answer += X / (2 + F*x)
    x += 1
    if len(outcomes) > 0 and answer > outcomes[-1]:
      f.write('Case #%d: %s\n' % (i, format(round(outcomes[-1], 7), ".7f")))
      break
    else:
      outcomes.append(answer)

f.close()
