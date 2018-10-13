def read_file(input):
  my_list = []
  test_case = []
  case = []
  file = open(input, 'r')
  for line in file:
    my_list.append(line.rstrip('\n').split(','))
  x = my_list.pop(0)

  for j in range (0,int(x[0])):
    test_case.append(my_list[0:10])

    del my_list[:10]
  print my_list
  return test_case

def magician(test_cases):
  counter = 0
  f = open('output.txt','w')
  for test_case in test_cases:
    counter += 1
    f_select = int(test_case[0][0])
    first_select = test_case[f_select][0].split()
    s_select = int(test_case[5][0]) + 5
    second_select = test_case[s_select][0].split()
    my_set = set(first_select).intersection(second_select)
    print my_set
    if len(list(my_set)) == 1:
      f.write( 'Case #%s: %s\n' % (counter,list(my_set)[0]))
    elif len(list(my_set)) == 0:
      f.write( 'Case #%s: Volunteer cheated!\n' % (counter))
    else:
      f.write( 'Case #%s: Bad magician!\n' % (counter))
  f.close()

if __name__ == "__main__":
  cases = read_file('A-small-attempt2.in')
  magician(cases)


