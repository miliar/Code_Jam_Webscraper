f = open('B.input.txt', 'r')
output = ""

T = int(f.readline())
for i in range(0, T):
  input = f.readline().split(' ')
  comb = {}
  opps = {}
  C = int(input[0])
  D = int(input[C + 1])
  N = int(input[C + D + 2])
  result = []
  
  for c in range(1, C + 1):
    comb[input[c][0:2]] = input[c][2]
    comb[input[c][1::-1]] = input[c][2]
    
  for d in range(C + 2, C + D + 2):
    if not input[d][0] in opps:
      opps[input[d][0]] = []
    opps[input[d][0]].append(input[d][1])
    
    if not input[d][1] in opps:
      opps[input[d][1]] = []
    opps[input[d][1]].append(input[d][0])    
  
  invoke = input[len(input) - 1][0:N]
  
  for n in range(0, len(invoke)):
    skip = False
    if len(result) > 0:
      pair = result[len(result) - 1] + invoke[n]
      if pair in comb:
        result.pop()
        result.append(comb[pair])
        skip = True
      elif invoke[n] in opps:
        for opp in opps[invoke[n]]:
          if opp in result:
            result = []
            skip = True
    if not skip:
      result.append(invoke[n])
  
  output = output + "Case #%d: %s" % (i + 1, '[' + ', '.join(result) + ']')
  output = output + "\n"
  

f = open('B.output.txt', 'w')
f.write(output)