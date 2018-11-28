input = [line[:-1] for line in file("in")][1:]

case = 0

def invoke_stuff(string):
  something_happened = True
  while something_happened:
    something_happened = False

    if len(string) < 2:
      break

    for comb in combinations:
      result = combinations[comb]
      if string[-2:] == comb or string[-2:][::-1] == comb:
        string = string[:-2] + result
        something_happened = True
        break

    for boom in booms:
      if boom[0] in string and boom[1] in string:
        string = ""
        break

  return string


for line in input:
  case += 1

  line = line.split(" ")
  count = int(line[0])
  arr_pos = 1

  magics = line[-1]

  combinations = {}
  booms = []

  for x in range(count):
    item = line[arr_pos]
    combinations[item[:2]] = item[2]
    arr_pos += 1

  count = int(line[arr_pos])
  arr_pos += 1

  for x in range(count):
    item = line[arr_pos]
    booms.append(item)
    arr_pos += 1

  string = ""
  for c in magics:
    string += c
    string = invoke_stuff(string)

  output = ", ".join([c for c in string])
  output = "[" + output + "]"

  print "Case #%d:" % case, output

