#!/usr/bin/python3
class Combine():
  def __init__(self, base_elements, derived_element):
    assert(len(base_elements) == 2)
    self.base_elements = list(base_elements)
    self.derived = derived_element

  def __str__(self,):
    return '{0}->{1}'.format(self.base_elements, self.derived)

  def contains(self, element1, element2):
    return(((element1 == self.base_elements[0])
            and (element2 == self.base_elements[1])) or 
           ((element2 == self.base_elements[0])
            and (element1 == self.base_elements[1])))

class Oppose():
  def __init__(self, elements):
    assert(len(elements) == 2)
    self.elements = list(elements)

  def __str__(self,):
    return '{0}'.format(self.elements)

  def contains(self, element1, element2):
    return(((element1 == self.elements[0])
            and (element2 == self.elements[1])) or 
           ((element2 == self.elements[0])
            and (element1 == self.elements[1])))

def parse_input(string):
  tokens = string.split()

  num_combines = int(tokens.pop(0))
  combines = tokens[:num_combines]

  num_opposed = int(tokens.pop(num_combines))
  opposed = tokens[num_combines:num_combines + num_opposed]

  orders = tokens[-1]

  return(combines, opposed, orders)

def make_combine_list(combine_strings):
  def create_combine(string):
    assert(len(string) == 3)
    return Combine(string[:2], string[2])

  list = []
  for combine_string in combine_strings:
    list.append(create_combine(combine_string))
  return list

def make_opposed_list(opposed_strings):
  list = []
  for opposed_string in opposed_strings:
    list.append(Oppose(opposed_string))
  return list

def try_combine(element1, element2, combine_list):
  for combine in combine_list:
    if (combine.contains(element1, element2)):
      return combine.derived

def check_opposed_list(order, element_list, opposed_list):
  for element in element_list:
    for oppose in opposed_list:
      if oppose.contains(order, element):
        return True

def play_turn(order, element_list, combine_list, opposed_list):
  # Do we have an empty list?
  if len(element_list) < 1:
    element_list.append(order)
    return

  # Can we make a combination from the back of the stack?
  combination = try_combine(element_list[-1], order, combine_list)
  if (combination):
    element_list.pop()
    element_list.append(combination)
    return

  # Does the new element oppose any on the stack?
  if (check_opposed_list(order, element_list, opposed_list)):
    # We have an opposition- clear the list
    del element_list[:]
    return

  # No reactions- just add it to the back
  element_list.append(order)

def run_case(input):
  (combines, opposed, orders) = parse_input(input)
  combine_list = make_combine_list(combines)
  opposed_list = make_opposed_list(opposed)

  for combine in combine_list:
    print(combine)
  for oppose in opposed_list:
    print(oppose)
  print(orders)

  element_list = []
  for order in orders:
    play_turn(order, element_list, combine_list, opposed_list)
    # print(element_list)
  return(element_list)

def format_list(element_list):
  string = '['
  if len(element_list) > 0:
    string += '{0}'.format(element_list.pop(0))
  for element in element_list:
    string += ', {0}'.format(element)
  string += ']'
  return string


def main(problem = ''):
  with open('{0}.out'.format(problem), 'w') as out_file:
    with open('{0}.in'.format(problem), 'r') as in_file:
      num_cases = in_file.readline()
      for case_num, line in enumerate(in_file.readlines(), 1):
        list = run_case(line)
        out_file.write('Case #{0}: {1}\n'.format(case_num, format_list(list)))
