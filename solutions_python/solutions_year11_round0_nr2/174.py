#f = open('B-small-attempt2.in', 'r')
f = open('B-large.in', 'r')
#f = open('B-practice.in', 'r')
out = open('B-small.out', 'w')

T = int(f.readline().strip())

for t in xrange(T):
  case = f.readline().strip().split(' ')
  C = int(case[0])
  combs_raw = [(x[0:2], x[2]) for x in case[1:C + 1]]
  combs = {}
  for a, b in combs_raw:
    combs[a] = b
  D = int(case[C + 1])
  opposed = case[C + 2:C + 2 + D]
  N = int(case[C + 2 + D])
  invoke = case[C + 2 + D + 1]

  #print C, combs, D, opposed, N, invoke
  
  def is_opposed(invoke, letter):
    for c in invoke:
      if c + letter in opposed or letter + c in opposed:
        return True
    return False
  
  def process_invoke(invoke_string):
    if len(invoke_string) < 1:
      return invoke_string
    
    pre_invoke = invoke_string[:-1]
    last_letter = invoke_string[-1]
    
    done_string = process_invoke(pre_invoke)
    
    if len(done_string) == 0:
      return last_letter
    
    comb1 = done_string[-1] + last_letter
    comb2 = last_letter + done_string[-1]
    if comb1 in combs:
      return done_string[:-1] + combs[comb1]
    elif comb2 in combs:
      return done_string[:-1] + combs[comb2]

    if (is_opposed(done_string, last_letter)):
      return ''
        
    return done_string + last_letter
  
  print 'Case #%d: ' % (t + 1) + str(list(process_invoke(invoke)))
  out.write('Case #%d: ' % (t + 1) + str(list(process_invoke(invoke))).replace('\'', '') + '\n')
  

f.close()
out.close()
