import sys

f = open('A-large.in', 'r')
o = open('A-large.out', 'w')

T = int(f.readline().rstrip('\n'))
i = 1
while i <= T:
  data = f.readline()
  max_shyness_level = int(data.split(' ')[0])
  lst = map(lambda x: int(x), list(data.split(' ')[1].rstrip('\n')))
  j = 1
  res = 0
  stood_up = 0
  while j <= max_shyness_level:
    stood_up += lst[j-1]
    if stood_up < j:
      needs = j - stood_up
      res += needs
      lst[0] += needs
      stood_up += needs
    j += 1
  o.write('Case #' + str(i) + ': ' + str(res) + '\n')
  i += 1
