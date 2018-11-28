def main():
  filename = "B-large.in"
  fh = open(filename, 'r')
  T = int(fh.readline())
  case = 1

  while T > 0:
    getInfo(fh, case)
    T = T - 1
    case = case + 1

def getInfo(fh, case):
  values = fh.readline().split()
  combos = []
  oppose = []

  for i in range(int(values[0])):
    combos.append(values[i+1])
  del(values[0:int(values[0])+1])

  for i in range(int(values[0])):
    oppose.append(values[i+1])
  del(values[0:int(values[0])+1])

  length = int(values[0])
  seq = values[1]

  cdict = {}
  odict = {}

  for i in combos:
    if cdict.has_key(i[0]):
      cdict[i[0]].append(i[1:])
    else:
      cdict[i[0]] = [i[1:]]
    if cdict.has_key(i[1]):
      cdict[i[1]].append(i[0]+i[2])
    else:
      cdict[i[1]] = [i[0]+i[2]]

  for i in oppose:
    if odict.has_key(i[0]):
      odict[i[0]].append(i[1])
    else:
      odict[i[0]] = [i[1]]
    if odict.has_key(i[1]):
      odict[i[1]].append(i[0])
    else:
      odict[i[1]] = [i[0]]

  final_list = []
  loc = 0

  while loc < length:
    if len(final_list) == 0:
      final_list.append(seq[loc])
      loc = loc + 1
      continue

    final_list.append(seq[loc])

    if cdict.has_key(final_list[-1]):
      for item in cdict[final_list[-1]]:
        if item[0] == final_list[-2]:
          del(final_list[-2])
          del(final_list[-1])
          final_list.append(item[1])
          break

    if odict.has_key(final_list[-1]):
      for item in odict[final_list[-1]]:
        if item[0] in final_list:
          final_list = []
          break

    loc = loc + 1

  answer = "["

  for i in final_list:
    answer = answer + i + ", "

  answer = answer[0:-2] + "]"

  if len(answer) == 1:
    answer = "[]"

  print "Case #" + str(case) + ": " + answer

main()





