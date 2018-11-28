#/bin/python.exe
import sys
""" Combined are in the form frozenset(cmb1, cmb2) -> result
    Opposed are in the form (op1, op2) (as a string) 
"""

def split_list(lst):
  return (lst[0], lst[1:])

def get_combines(arr_input):
  num_combines, rest = split_list(arr_input)
  combines = dict([(frozenset([cmb[0], cmb[1]]), cmb[2]) for cmb in 
              rest[:int(num_combines)]])
  return (combines, rest[int(num_combines):])

def get_opposed(arr_input):
  num_opposed, rest = split_list(arr_input)
  opposed = rest[:int(num_opposed)]
  return (opposed, rest[int(num_opposed):])

def invoke_sequence(combines, opposed, in_list, to_do):
  if len(to_do) == 0: return in_list
  head, rest = split_list(to_do)
  if len(in_list) == 0:
    result_list = [head]
  else:
    last_in = in_list[-1]
    #check for combines
    combine_key = frozenset([last_in, head])
    if combine_key in combines:
      #replace last element
      result_list =in_list[:-1] + [combines[combine_key]]
    else:
      #check for opposed
      head_opposed_to = [op[1] if op[0] == head else op[0] for
                            op in opposed if head in op]
      if len(frozenset(head_opposed_to) & frozenset(in_list)) > 0: 
        #one of conflicting elements is in the list, so clear
        result_list = []
      else:
        #append list
        result_list = in_list + [head]
  
  return invoke_sequence(combines, opposed, result_list, rest)

def solve_case(line_input):
  combines, rest = get_combines(line_input.strip().split(" "))
  opposed, rest = get_opposed(rest)
  to_invoke = list(rest[1]) #ignore size argument
  return "[%s]" % (", ".join(invoke_sequence(
    combines, opposed, [], to_invoke)))

#main
input_f = open(sys.argv[1])
num_cases = int(input_f.readline())
for c in xrange(1, num_cases+1):
  print "Case #%d: %s" % (c, solve_case(input_f.readline()))

