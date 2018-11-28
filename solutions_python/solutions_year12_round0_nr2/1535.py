# mrtwiddletoes
inp = open('/home/thinkbot/src/random/codejam/B-small-attempt1.in', 'r')
out = open('/home/thinkbot/src/random/codejam/output.out', 'w')
num_trials = inp.readline()
for a in range(int(num_trials)):
  data = inp.readline().split(' ')
  num_googlers = int(data[0])
  surprising = int(data[1])
  min_score = int(data[2])
  min_unsurprising = min_score * 3 - 2
  min_surprising = min_score * 3 - 4
  if surprising > min_surprising:
    min_surprising = surprising
  unsurprising = 0
  possible = 0
  for x in range(3, len(data)):
    if int(data[x]) >= min_unsurprising:
      unsurprising += 1
    elif int(data[x]) >= min_surprising:
      possible += 1
  if possible > surprising:
    possible = surprising
  result = unsurprising + possible
  out.write('Case #{0}: {1}\n'.format(a+1, result))
