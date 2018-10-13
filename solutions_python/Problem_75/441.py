import sys

input = sys.stdin
N = int(input.readline())
for n in xrange(1,N+1):
  data = input.readline().strip().split(' ')

  comb_count = int(data[0])
  offset = 1
  combs = data[offset : offset + comb_count]

  comb_dict = {}
  for comb in combs:
    comb_dict[comb[:2]] = comb[-1]

  opp_count = int(data[offset + comb_count])
  offset = offset + comb_count + 1
  opps = set(data[offset : offset + opp_count])

  inv = list(data[-1])

  #print combs, comb_dict, opps, inv

  element = []
  for i in inv:
    element.append(i)

    if len(element) > 1:
      etail = element[-1] + element[-2]
      retail = element[-2] + element[-1]

      if etail in comb_dict:
        element = element[:-2] + list(comb_dict[etail])
      elif retail in comb_dict:
        element = element[:-2] + list(comb_dict[retail])
      else:
        t = element[-1]
        for a in element:
          if a+t in opps or t+a in opps:
            element = []
            break
    #print element
  print 'Case #%d: [%s]'%(n, ', '.join(element))


