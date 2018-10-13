


with open('output.txt', 'wb') as output_file:
  with open('A-small-attempt1.in.txt', 'rb') as input_file:
  # with open('input.txt', 'rb') as input_file:
    next(input_file)
    case_number = 1
    for line in input_file:
      max_thing, number_string = line.strip().split(' ')
      res = 0
      people_we_have = 0
      for i, c in enumerate(number_string):
        # if i == 0 and c == '0':
        #   res += 1
        if people_we_have > max_thing:
          break
        elif c != '0' and people_we_have < i:
          res += i - people_we_have 
          people_we_have += res + int (c)
        else:
          people_we_have += int(c)

      print "{} {}".format(number_string, res)
      output_file.write("Case #{}: {}\n".format(case_number, res))
      case_number += 1