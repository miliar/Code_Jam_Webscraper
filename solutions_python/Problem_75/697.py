
def invoke(combine, opposed, elements):
  combine_hash = {}
  for elem in combine:
    combine_hash[elem[0]+elem[1]] = elem[2]
    combine_hash[elem[1]+elem[0]] = elem[2]
  opposed_hash = {}
  for elem in opposed:
    opposed_hash[elem[0]] = elem[1]
    opposed_hash[elem[1]] = elem[0]
  invoke_list = []
  for elem in elements:
    invoke_list.append(elem)
    while len(invoke_list) > 1:
      tail_element = invoke_list[-2] + invoke_list[-1]
      if tail_element in combine_hash:
        invoke_list.pop()
        invoke_list.pop()
        invoke_list.append(combine_hash[tail_element])
      elif invoke_list[-1] in opposed_hash and opposed_hash[invoke_list[-1]] in invoke_list:
        invoke_list = []
        break
      else:
        break
    
  return invoke_list

if __name__ == '__main__':
  num_of_cases = int(raw_input())
  for case_index in range(num_of_cases):
    data = raw_input().strip().split()
    combine = []
    for i in range(int(data.pop(0))):
      combine.append(data.pop(0))

    opposed = []
    for i in range(int(data.pop(0))):
      opposed.append(data.pop(0))

    data.pop(0)
    elements = data.pop(0)

    casted_elements = invoke(combine, opposed, elements)
    print "Case #%d: [%s]" % (case_index+1, ", ".join(casted_elements))
