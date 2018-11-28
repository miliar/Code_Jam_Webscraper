def guests(max_shyness, audience):
  if max_shyness == 0:
    return 0
  shy_level = 0
  curr_level = 0
  additions = 0
  for each in str(audience):
    each = int(each)
    curr_level += each
    if (shy_level >= curr_level):
      difference = shy_level-curr_level+1
      curr_level += difference
      additions += difference
    shy_level += 1
  return additions

def run(input_file, output_file):
  f = open(input_file, 'r')
  tests = []
  for line in f:
    tests.append(line)
  results = []
  case = 0
  for each in tests:
    if case == 0:
      case += 1
      continue
    else:
      each = each.split()
      max_shyness = each[0]
      audience = each[1]
      result = guests(max_shyness, audience)
      results.append([case, result])
      case += 1 
  g = open(output_file, 'w')
  for each in results:
    g.write("Case #" + str(each[0]) + ": " + str(each[1]))
    g.write("\n")
  g.close()
