def flip_range(states,i,j):
  for k in xrange(i,j):
    states[k] = not states[k]

def solve(input):
  parts = input.strip().split(" ")
  K = int(parts[1])
  flipstates = [ch == '+' for ch in parts[0]]
  ls = len(flipstates)
  count = 0
  for i in xrange(ls):
    state = flipstates[i]
    if state == False:
      if i + K <= ls:
        count += 1
        flip_range(flipstates,i,i+K)
      else:
        return "IMPOSSIBLE"
        
  return str(count)
      

def main():
  name = "A-large"
  lines = open(name+'.in').read().split("\n")
  out = []
  for i, line in enumerate(lines[1:]):
    if len(line) > 1:
      out.append("Case #%i: %s" % (i+1, solve(line)))

  open(name+'.out','w').write("\n".join(out))
    
main()